from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Your Account Sid and Auth Token
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Provide actions for the new task
support_ticket_actions = {
    'actions': [
        {'say': 'This is where I could pull in the ticket status via api or some call like that.'}
    ]
}

# Create a new task named 'tell_a_joke'
task = client.autopilot \
    .assistants('UAff63b037fde138336d4a8f88ef502460') \
    .tasks \
    .create(
        unique_name='support-ticket-request',
        actions=support_ticket_actions)

phrases = [
    'Check on my support ticket',
    'check on my support ticket',
    'support ticket',
    'Support ticket',
    'ticket',
    'Ticket'
]

for phrase in phrases:
    sample = client.autopilot \
        .assistants('UAff63b037fde138336d4a8f88ef502460') \
        .tasks('support-ticket-request') \
        .samples \
        .create(language='en-us', tagged_text=phrase)