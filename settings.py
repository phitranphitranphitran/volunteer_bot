import os
from dotenv import load_dotenv


load_dotenv()


PORT = os.getenv("PORT")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
