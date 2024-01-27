import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["سورس","السورس","المصنع"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/ca112cdaee8107668dd9d.jpg",
        caption=f"""| مطور السورس \n| مطور البوت""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور السورس .", url=f"https://t.me/rr8r9"),
                ],
                [
                   InlineKeyboardButton(
                        "- مطور البوت ", url=f"https://t.me/xl444"),
                ],       
            ]
        ),
    )