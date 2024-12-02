from utils import generate_verification_token
import os
import json
import boto3
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def get_secret():
    secret_name = os.environ['SECRETS_ARN']
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=os.environ['AWS_REGION']
    )
    
    try:
        response = client.get_secret_value(SecretId=secret_name)
        secrets = json.loads(response['SecretString'])
        print("Successfully retrieved secrets")
        return secrets
    except Exception as e:
        print(f"Error retrieving secret: {str(e)}")
        raise e

def lambda_handler(event, context):
    try:
        # Get secrets first
        secrets = get_secret()
        
        # Parse the SNS message
        for record in event['Records']:
            sns_message = json.loads(record['Sns']['Message'])
            print(f"Processing verification for user: {sns_message['user_id']}")
            
            # Generate verification token
            token = generate_verification_token(
                sns_message['user_id'],
                secrets['SECRET_TOKEN']
            )
            
            # Construct verification URL
            verification_url = f"https://demo.{os.environ['DOMAIN_NAME']}/v1/user/verify?token={token}"
            
            # Construct email
            email = Mail(
                from_email=secrets['sender_email'],
                to_emails=sns_message['email'],
                subject='Verify Your Account',
                html_content=f'Please verify your account by clicking on this link: {verification_url}'
            )
            
            # Send email
            sg = SendGridAPIClient(secrets['sendgrid_api_key'])
            response = sg.send(email)
            print(f"SendGrid Response Status Code: {response.status_code}")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Email sent successfully!')
        }
            
    except Exception as e:
        print(f"Error in lambda_handler: {str(e)}")
        print(f"Event received: {json.dumps(event)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }