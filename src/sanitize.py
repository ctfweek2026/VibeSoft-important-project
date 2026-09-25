import re

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
    