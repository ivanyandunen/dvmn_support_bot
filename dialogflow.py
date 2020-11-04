import json
import dialogflow_v2 as dialogflow
from dotenv import load_dotenv
import os
import argparse


def get_parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-q', '--questions',
        default='questions.json',
        help='Specify a file with train phrases. Default is "questions.json".'
    )
    return parser.parse_args()


def detect_intent_texts(project_id, session_id, text, language_code='ru-RU'):

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code
    )
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = session_client.detect_intent(
        session=session, query_input=query_input
    )
    return response


def load_questions(file):
    with open(file, "r") as file_object:
        questions = json.load(file_object)
    return questions


def create_intent(intent_name, training_phrases_parts, message_texts, project_id):
    client = dialogflow.IntentsClient()
    parent = client.project_agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.types.Intent.TrainingPhrase.Part(
            text=training_phrases_part)
        training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.types.Intent.Message.Text(text=message_texts)
    message = dialogflow.types.Intent.Message(text=text)

    intent = dialogflow.types.Intent(
        display_name=intent_name,
        training_phrases=training_phrases,
        messages=[message])

    return client.create_intent(parent, intent)


def train_agent(project_id):
    client = dialogflow.AgentsClient()
    parent = client.project_path(project_id)
    client.train_agent(parent)


if __name__ == "__main__":

    load_dotenv()

    project_id = os.getenv('PROJECT_ID')
    args = get_parser_args()

    questions = load_questions(args.questions)

    for intent_name, data in questions.items():
        questions = data['questions']
        answer = data['answer']
        create_intent(intent_name, questions, [answer], project_id=project_id)

    train_agent(project_id)
