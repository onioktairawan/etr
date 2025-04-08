import json
import datetime


def format_uptime(seconds: int) -> str:
    return str(datetime.timedelta(seconds=seconds))


def load_json(path: str) -> dict:
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_json(path: str, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)


def markdown_escape(text: str) -> str:
    escape_chars = r"\_*[]()~`>#+-=|{}.!"
    for char in escape_chars:
        text = text.replace(char, "\\" + char)
    return text
