# Volunteer Bot

Slack bot for picking volunteers.

## Installation

```
# Install pipenv if not already installed
pip install pipenv

# Then clone the project
git clone ...
cd volunteer_bot

# Install dependencies
pipenv install

# Fill in your settings into .env
cp .env.example .env

# Run the app
pipenv run python app.py

# To connect with Slack you can use ngrok (in another shell tab)
ngrok http 3000
```