import os

def get_secret_key():
    return os.getenv("APP_SECRET_KEY", "default-dev-key")

def add(a: int, b: int) -> int:
    return a + b