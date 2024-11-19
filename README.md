# Lambda Function for Account Verification

This project is designed to send account verification emails via AWS Lambda, triggered by AWS Simple Notification Service (SNS). It generates a unique verification token for each user and sends an email containing the verification link using SendGrid.

## About AWS Lambda Function

### What is AWS Lambda?

AWS Lambda is a serverless compute service that runs your code in response to events, such as changes in data or system state, without the need to provision or manage servers. You simply upload your code, and Lambda automatically manages the compute resources required to run it.

In this project, we use AWS Lambda to listen for SNS messages, process them, generate a verification token, and send an email using SendGrid. The Lambda function is designed to automatically scale based on the number of messages it receives and does not require manual infrastructure management.

This project consists of two main files:
1. `lambda_function.py`: AWS Lambda function that listens for SNS messages, generates a verification token, and sends an email to the user.
2. `utils.py`: Utility file containing a function to generate a unique verification token for the user.

## Prerequisites

Before using the Lambda function, make sure you have the following:

- **AWS Lambda**: Set up an AWS Lambda function.
- **AWS SNS**: The Lambda function is triggered by SNS messages.
- **SendGrid Account**: You need a SendGrid account for email sending.
- **Environment Variables**: The following environment variables need to be set:
  - `SENDGRID_API_KEY`: Your SendGrid API key for sending emails.
  - `SENDER_EMAIL`: The email address from which verification emails will be sent.
  - `DOMAIN_NAME`: The domain name used in the verification URL.

### Installation

1. Install required Python packages by using `pip`:
   ```bash
   pip install sendgrid

#### Key Features:
- **Triggering by SNS**: The Lambda function listens for SNS messages. Each message contains `user_id` and `email`.
- **Token Generation**: The function generates a unique verification token using the `user_id` and a random UUID.
- **Email Sending**: The function uses the SendGrid API to send an email containing a verification link to the user’s email.
- **Error Handling**: If the email fails to send, the function logs the error and returns an HTTP status code of 500. If successful, it returns a status code of 200.

