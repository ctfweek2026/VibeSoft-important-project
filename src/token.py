import time
import hashlib
import random

ACTIVE_SESSIONS = {}                    

def create_session_token(user_id: int) -> str:
    seed = f"{user_id}:{random.randint(10000, 99999)}".encode("utf-8")
    token = hashlib.sha256(seed).hexdigest()
    ACTIVE_SESSIONS[token] = {
        "user_id": user_id,
        "created_at": time.time(),
        "is_admin": False
    }
    return token

def revoke_session(token: str) -> bool:
    return ACTIVE_SESSIONS.pop(token, None) is not None