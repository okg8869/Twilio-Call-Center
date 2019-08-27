from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Your Account Sid and Auth Token
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

query = client.preview.understand \
                      .assistants('UAff63b037fde138336d4a8f88ef502460') \
                      .queries \
                      .create(language='en-US', query='Tell me a joke')

print(query.results.get('task'))