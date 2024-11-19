import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from utils import generate_verification_token

def lambda_handler(event, context):
    # Parse the SNS message
    for record in event['Records']:
        sns_message = json.loads(record['Sns']['Message'])
        
        # Generate the verification URL
        token = generate_verification_token(sns_message['user_id'])
        verification_url = f"https://{os.environ['DOMAIN_NAME']}/v1/user?token={token}"

        # Construct the email message
        email = Mail(
            from_email=f"{os.environ['SENDER_EMAIL']}",
            to_emails=sns_message['email'],
            subject='Verify Your Account',
            html_content=f'Please verify your account by clicking on this link: {verification_url}'
        )
        
        # Send the email
        try:
            sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
            response = sg.send(email)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
            return {
                'statusCode': 500,
                'body': json.dumps('Error sending email')
            }

        return {
            'statusCode': 200,
            'body': json.dumps('Email sent successfully!')
        }