from decouple import config


PORT = config("PORT", cast=int)
SLACK_BOT_TOKEN = config("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = config("SLACK_SIGNING_SECRET")
