import uuid

def generate_verification_token(user_id):
    # Generate a unique token incorporating the user_id
    unique_part = uuid.uuid4().hex  # Generates a random UUID
    token = f"{user_id}-{unique_part}"
    return token
