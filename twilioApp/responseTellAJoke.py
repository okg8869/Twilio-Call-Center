from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Your Account Sid and Auth Token
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Provide actions for the new task
joke_actions = {
    'actions': [
        {'say': 'I was going to look for my missing watch, but I could never find the time.'}
    ]
}

# Create a new task named 'tell_a_joke'
task = client.autopilot \
    .assistants('UAff63b037fde138336d4a8f88ef502460') \
    .tasks \
    .create(
        unique_name='tell-a-joke',
        actions=joke_actions)

phrases = [
    'Tell me a joke',
    'Tell me a joke',
    'I\'d like to hear a joke',
    'Do you know any good jokes?',
    'Joke',
    'Tell joke',
    'Tell me something funny',
    'Make me laugh',
    'I want to hear a joke',
    'Can I hear a joke?',
    'I like jokes',
    'I\'d like to hear a punny joke'
]

for phrase in phrases:
    sample = client.autopilot \
        .assistants('UAff63b037fde138336d4a8f88ef502460') \
        .tasks('tell-a-joke') \
        .samples \
        .create(language='en-us', tagged_text=phrase)