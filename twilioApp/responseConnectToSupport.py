from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Your Account Sid and Auth Token
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Provide actions for the new task
support_connect_actions = {
    'actions': [
        {'say': 'I would probably use the studio to actually route some of these decisions if this was a live flow.'}
    ]
}

# Create a new task named 'tell_a_joke'
task = client.autopilot \
    .assistants('UAff63b037fde138336d4a8f88ef502460') \
    .tasks \
    .create(
        unique_name='connect-to-support',
        actions=support_connect_actions)

phrases = [
    'Tell me a joke',
]

for phrase in phrases:
    sample = client.autopilot \
        .assistants('UAff63b037fde138336d4a8f88ef502460') \
        .tasks('connect-to-support') \
        .samples \
        .create(language='en-us', tagged_text=phrase)