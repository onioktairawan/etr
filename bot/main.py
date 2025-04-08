# bot/main.py
import asyncio
from pyrogram import Client
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

bot = Client(
    "bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={"root": "bot"}  # agar handler di folder bot otomatis dikenali
)

if __name__ == "__main__":
    bot.run()
