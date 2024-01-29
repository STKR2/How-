import asyncio
import random
import os
import time
import requests
from random import  choice, randint
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["سورس","السورس","المبرمج"])
    & filters.group
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/94fa4bb62424ea712eaa2.jpg",
        caption=f"""-| مطور السورس \n-| قناة المطور""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور السورس .", url=f"https://t.me/rr8r9"),
                ],
                [
                   InlineKeyboardButton(
                        "- قناة المطور ", url=f"https://t.me/xl444"),
                ],       
            ]
        ),
    )

@app.on_message(command(["اقتباسات", "اقتباس"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/alaaa/{rl}"
    await client.send_photo(message.chat.id,url,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
