# Bots for Telegram and Vk.com with Dialogflow.com support

## Description
Here are two chatbots for telegram and vk.com which could be used as first-line support in your channel/community.

## How to use
### Dialogflow
[Create a project in Dialogflow](https://cloud.google.com/dialogflow/docs/quick/setup)

[Create a new agent ](https://cloud.google.com/dialogflow/docs/quick/build-agent)

### Telegram
Create new bot with help of [@BotFather](https://t.me/BotFather)

### Vk.com
[Create new community](https://vk.com/groups?tab=admin) and get token in it's API settings

## How to run bots locally
Create file .env in the same directory with scripts and enter tokens your got above.
```
PROJECT_ID= project id in Dialogflow
TG_TOKEN= telegram bot's token
VK_TOKEN= vk bot's token
```
Python3 has to be installed.

Run
```
pip install -r requirements.txt
```
Then for starting telegram bot:
```
python3 tg_support_bot.py
```
for starting vk bot:
```
python3 vk_support_bot.py
```

### To train dialogflow agent with new phrases
Phrases are saved in **quiestions.json**
```
python3 dialogflow.py
```
