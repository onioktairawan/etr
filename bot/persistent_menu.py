# bot/persistent_menu.py
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup

@Client.on_message(filters.command("start"))
async def show_persistent_menu(client, message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            ["📊 Status Akun", "🔄 Reset Ubot"],
            ["🧬 Ganti Prefix", "🔠 Reset Emoji"],
            ["🧩 Cek Fitur", "📚 Panduan"],
            ["🎯 Pasang Ubot", "🚪 Keluar"]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

    await message.reply(
        "Selamat datang! Silakan pilih menu di bawah ini:",
        reply_markup=keyboard
    )
