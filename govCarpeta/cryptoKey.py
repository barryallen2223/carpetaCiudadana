import os
from cryptography.fernet import Fernet

def generate_unique_key():
    key = Fernet.generate_key()
    return key.decode()
