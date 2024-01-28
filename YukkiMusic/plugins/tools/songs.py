import os
import asyncio
import yt_dlp
import requests

from ... import app
from strings.filters import command
from pyrogram import Client, filters
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch


@app.on_message(command(["بحث", f"يوت"]))
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
        

@app.on_message(
    command(["انضم", f"ادخل"]))
async def join_chat(c: Client, m: Message):
    chat_id = m.chat.id
    try:
        invitelink = (await c.get_chat(chat_id)).invite_link
        if not invitelink:
            await c.export_chat_invite_link(chat_id)
            invitelink = (await c.get_chat(chat_id)).invite_link
        if invitelink.startswith("https://t.me/+"):
            invitelink = invitelink.replace(
                "https://t.me/+", "https://t.me/joinchat/"
            )
        await user.join_chat(invitelink)
        await remove_active_chat(chat_id)
        return await user.send_message(chat_id, "✅ فرحان هوايه لان دزيتولي دعوة")
    except UserAlreadyParticipant:
        return await user.send_message(chat_id, "✅ موجود يمعود")
