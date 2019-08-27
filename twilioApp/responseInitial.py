from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Your Account Sid and Auth Token
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

# Build task actions for initial greating
initial_response_task_actions = {
    'actions': [
        {'say': '''Hello and welcome to COMPANY_NAME support! 
                If you would like to stop recieving these messages,
                just reply with "Quit" to unsubscribe. 
                Tell us a little about what you are looking for! 
                You can reply with things like "Check on my support ticket", "Connect me with a support rep", or even "Tell me a joke!" '''},
        {'listen': True}
    ]
}


# Create the hello_world task
task = client.autopilot.assistants('UAff63b037fde138336d4a8f88ef502460') \
                       .tasks \
                       .create(
                           unique_name='initial-hello',
                           actions=initial_response_task_actions)

# Set responses to listen for
responses = [
    'hello',
    'hi',
    'Hello',
    'Hi there'
]

# Run initial-hellotask based on response
for response in responses:
    sample = client.autopilot \
        .assistants('UAff63b037fde138336d4a8f88ef502460') \
        .tasks('initial-hello') \
        .samples \
        .create(language='en-us', tagged_text=response)

# Set initial-hello as the default task for support-chatbot
defaults = client.autopilot \
                 .assistants('UAff63b037fde138336d4a8f88ef502460') \
                 .defaults() \
                 .update(defaults={
                      'defaults': {
                          'assistant_initiation': 'task://initial-hello',
                          'fallback': 'task://intial-hello'
                      }
                  })


