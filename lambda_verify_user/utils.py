import uuid
import os

def generate_verification_token(user_id):
    # Generate a unique token incorporating the user_id
    token = f"{user_id}{os.environ['SECRET_TOKEN']}"
    return token
