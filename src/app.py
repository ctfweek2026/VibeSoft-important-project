import re
import time

def sanitize_username(raw_name: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_-]", "", raw_name.strip())
    if len(cleaned) < 3:
        raise ValueError("Username must be at least 3 characters long.")
    return cleaned.lower()

def mask_email(email: str) -> str:
    if "@" not in email:
        return email
    user, domain = email.split("@", 1)
    if len(user) <= 2:
        masked_user = user[0] + "*"
    else:
        masked_user = user[0] + ("*" * (len(user) - 2)) + user[-1]
    return f"{masked_user}@{domain}"

class SystemLogger:
    def __init__(self, prefix: str = "SYS"):
        self.prefix = prefix

    def _timestamp(self) -> str:
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    def info(self, message: str) -> None:
        print(f"[{self._timestamp()}] [{self.prefix}] [INFO]: {message}")

    def warn(self, message: str) -> None:
        print(f"[{self._timestamp()}] [{self.prefix}] [WARN]: {message}")

logger = SystemLogger(prefix="AUTH")

STATUS_MAPPINGS = {
    100: "INITIALIZING",
    200: "READY_FOR_CONNECTIONS",
    301: "MAINTENANCE_REQUIRED",
    400: "INVALID_PAYLOAD",
    500: "INTERNAL_FATAL_ERROR",
}

def describe_status(code: int) -> str:
    return STATUS_MAPPINGS.get(code, "UNKNOWN_STATUS_CODE")