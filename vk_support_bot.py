import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
import os
import random
from dialogflow import detect_intent_texts
import logging
from tg_logger import TgHandler


logger = logging.getLogger("Logger")


def reply_to_message(event, vk_api):
    response = detect_intent_texts(project_id, f'vk-{event.user_id}', event.text)
    if not response.query_result.intent.is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=response.query_result.fulfillment_text,
            random_id=random.randint(1,1000)
        )


if __name__ == "__main__":

    load_dotenv()

    logger.setLevel(logging.INFO)
    logger.addHandler(TgHandler())

    project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
    vk_session = vk_api.VkApi(token=os.getenv('VK_TOKEN'))
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            if event.to_me:
                reply_to_message(event, vk_api)
            else:
                print('От меня для: ', event.user_id)
            print('Текст:', event.text)
