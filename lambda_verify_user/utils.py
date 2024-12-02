#import uuid
import os

def generate_verification_token(user_id,secret_token):
    # Generate a unique token incorporating the user_id
    token = f"{user_id}{secret_token}"
    return token
