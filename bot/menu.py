# bot/menu.py
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import json
import os
from datetime import datetime, timedelta
import time

from shared.database import get_user_data

start_time = time.time()

HEADER = (
    "🤖 𝐔𝐛𝐨𝐭 - 𝐈𝐧𝐥𝐢𝐧𝐞 𝐇𝐞𝐥𝐩\n"
    "🔤 Prefixes: . ? + !\n"
    "📦 Plugins: 1 - 1000\n"
    "👤 User: @{username}\n"
    "🤖 Ubot by : Serpa\n\n"
)

def format_duration(seconds):
    return str(timedelta(seconds=int(seconds)))

@Client.on_message(filters.command(["start", "menu", "cekfitur", "fitur"], prefixes=["/", ".", "?", "!"]))
async def menu_handler(client: Client, message: Message):
    user_id = str(message.from_user.id)
    username = message.from_user.username or "anonymous"
    user_data = get_user_data(user_id)

    prefix = user_data.get("prefix", ".")
    is_premium = user_data.get("premium", False)
    expired = user_data.get("expired") or "-"

    if expired != "-":
        expired = datetime.strptime(expired, "%Y-%m-%d %H:%M:%S")
        expired_str = expired.strftime("%Y-%m-%d %H:%M")
    else:
        expired_str = "-"

    uptime = format_duration(time.time() - start_time)

    fitur = (
        "• 💤 AFK         • 👮 Admin\n"
        "• 👁️ AutoRead    • 📣 AutoBC\n"
        "• 👶 Age         • 🕌 Adzan\n"
        "• 🎞️ Animasi    • 🥤 Asupan\n"
        "• 🔍 BingAI     • 🧠 ChatGPT\n"
        "• 📢 Broadcast  • ♊ Gemini\n"
        "• 🌀 Convert     • 😄 Emoji\n"
        "• 🌐 Global      • 🕘 History\n"
        "• ℹ️ Info        • 🅿️ Prefix\n"
        "• 🚪 PM Permit   • 🖼️ Sticker\n"
        "• 🏷️ Tag All     • 💬 Chats"
    )

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📃 Saya Setuju", callback_data="agree"),
            InlineKeyboardButton("🏠 Menu Utama", callback_data="mainmenu")
        ],
        [
            InlineKeyboardButton("⬅️ Prev", callback_data="prevmenu"),
            InlineKeyboardButton("➡️ Next", callback_data="nextmenu")
        ]
    ])

    text = HEADER.replace("{username}", username)
    text += (
        f"🛠️ Status Ubot: Aktif\n"
        f"👤 Status Pengguna: {'Customer' if is_premium else 'Free User'}\n"
        f"🔤 Prefix: {prefix}\n"
        f"⏳ Kedaluwarsa: {expired_str}\n"
        f"⏱️ Uptime: {uptime}\n\n"
        f"{fitur}"
    )

    await message.reply(text, reply_markup=keyboard)

