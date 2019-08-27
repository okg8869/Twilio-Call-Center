from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Your Account Sid and Auth Token
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
client = Client(account_sid, auth_token)

model_build = client.autopilot \
                    .assistants('UAa7b4faeccb05fda37801c9206cbe76e3') \
                    .model_builds \
                    .create(unique_name='v0.3')

print(model_build.sid)