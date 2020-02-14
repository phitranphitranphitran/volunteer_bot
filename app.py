import slack
from slackeventsapi import SlackEventAdapter

from settings import *

client = slack.WebClient(token=SLACK_BOT_TOKEN)
slack_events_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, endpoint="/slack/events")


@slack_events_adapter.on("reaction_added")
def reaction_added(event_data):
    emoji = event_data["event"]["reaction"]
    print(emoji)


@slack_events_adapter.on("app_mention")
def pick_volunteer(event_data):
    text = event_data["text"]
    user = event_data["user"]
    channel = event_data["channel"]
    response_text = "I choose you"
    client.chat_postMessage(channel=channel, text=response_text)


# Start the server
slack_events_adapter.start(port=PORT)
