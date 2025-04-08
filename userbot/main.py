# userbot/main.py
from pyrogram import Client, filters
import os

api_id = int(os.getenv("API_ID", 123456))
api_hash = os.getenv("API_HASH", "your_api_hash")

# Jika ingin login ulang, hapus file session_userbot.session
app = Client("session_userbot", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("ping") & filters.me)
async def ping_handler(client, message):
    await message.reply("Pong dari userbot!")

if __name__ == "__main__":
    print("[ USERBOT ] Aktif!")
    app.run()
