from pyrogram import Client
from menu import *

app = Client(
    "bot",
    api_id=123456,
    api_hash="your_api_hash",
    bot_token="your_bot_token"
)

if __name__ == "__main__":
    app.run()
