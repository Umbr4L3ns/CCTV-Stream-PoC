import base64

def decode_token(b64_token: str) -> str:
    """Decode base64 API token before injecting into RTSP header."""
    try:
        return base64.b64decode(b64_token.encode('ascii')).decode('utf-8')
    except Exception:
        return ""
