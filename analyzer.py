import os
import requests
from dotenv import load_dotenv
from utils.auth_helper import decode_token

load_dotenv()

TARGET_HOST = os.getenv("TARGET_HOST")
API_USER = os.getenv("API_USER")
API_TOKEN_B64 = os.getenv("API_TOKEN_B64")

def connect_stream():
    if not API_TOKEN_B64:
        print("[-] Error: API_TOKEN_B64 missing from environment.")
        return
    raw_token = decode_token(API_TOKEN_B64)
    print(f"[*] Authenticating to {TARGET_HOST} as {API_USER}...")
    # Session override logic

if __name__ == "__main__":
    connect_stream()
