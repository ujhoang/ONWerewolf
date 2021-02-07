import slack
import os
from pathlib import Path 
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter
import time


lobby = "C01KW0C1AQ6"
bot_uid = "U01KZQSBYMB"

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events', app) #handle different events sent from slack

client = slack.WebClient(token = os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
game_players = ["U01L2V25XJP","U01L8U1PAAY"]



@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        if "start" in text:
            game_room_uid = 'C01KXCXQN94'
            invite_response = client.conversations_invite(channel=game_room_uid, users=game_players)

            
            
            conversation_response = client.conversations_history(channel = game_room_uid, limit=300)
            while len(conversation_response.get("messages")) > 0:
                list_ts = list()
                for item in conversation_response.get("messages"):
                    list_ts + [item.get("ts")]
                
                for item_ts in list_ts:
                    delete_response = client.chat_delete(channel= game_room_uid, ts= item_ts)
            
            for person in game_players:
                kick_response = client.conversations_kick(channel=game_room_uid, user=person)


        

if __name__ == "__main__":
    app.run(debug=True)