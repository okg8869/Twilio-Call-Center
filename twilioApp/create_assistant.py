# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()


# Account Sid and Auth Token
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

assistant = client.autopilot \
                  .assistants \
                  .create(
                       friendly_name='Support Assistant 2.0',
                       unique_name='support_assistant_2'
                   )