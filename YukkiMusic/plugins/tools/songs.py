import os
import asyncio
import yt_dlp
import requests

from ... import app
from strings.filters import command
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch


@app.on_message(command(["يوت"], ["تحميل", "بحث", "تنزيل"]))
async def song(client: app, message: Message):
    aux = await message.reply_text("‹ جاري البحث  ›")
    if len(message.command) < 2:
        return await aux.edit(
            "‹ ارسل يوت واسم الملف الصوتي  ›"
        )
    try:
        song_name = message.text.split(None, 1)[1]
        vid = VideosSearch(song_name, limit = 1)
        song_title = vid.result()["result"][0]["title"]
        song_link = vid.result()["result"][0]["link"]
        ydl_opts = {
            "format": "mp3/bestaudio/best",
            "verbose": True,
            "geo-bypass": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3"
                }
            ],
            "outtmpl": f"downloads/{song_title}",
        }
        await aux.edit("‹ يتم الرفع  ›")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(song_link)
        await aux.edit("‹ تم التحميل  ›")
        await message.reply_audio(f"downloads/{song_title}.mp3")
        try:
            os.remove(f"downloads/{song_title}.mp3")
        except:
            pass
        await aux.delete()
    except Exception as e:
        await aux.edit(f"**Error:** {e}")


