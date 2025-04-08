import os
from utils.helper import load_json, save_json

DB_PATH = "shared/users.json"

# Load data awal
users = load_json(DB_PATH)

def get_user(user_id: str):
    return users.get(str(user_id), {
        "premium": False,
        "expired": None,
        "prefix": "."
    })

def set_user(user_id: str, data: dict):
    users[str(user_id)] = data
    save_json(DB_PATH, users)

def update_user(user_id: str, **kwargs):
    user = get_user(user_id)
    user.update(kwargs)
    set_user(user_id, user)

def is_premium(user_id: str):
    return get_user(user_id).get("premium", False)

def get_expired(user_id: str):
    return get_user(user_id).get("expired", None)

def get_prefix(user_id: str):
    return get_user(user_id).get("prefix", ".")
