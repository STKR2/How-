from __future__ import unicode_literals

import os

import requests
import yt_dlp
from strings.filters import command
from pyrogram import Client, filters
from YukkiMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL


ydl_opts = {
    "format": "best",
    "keepvideo": True,
    "prefer_ffmpeg": False,
    "geo_bypass": True,
    "outtmpl": "%(title)s.%(ext)s",
    "quite": True,
}



@app.on_message(command(["بحث","يوت","تحميل صوت","yt"]) & ~filters.private & ~BANNED_USERS)
def song(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("- **ابشر جاري البحث ..**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("- **معليش ما لقيت شي تأكد من كتابة اسم الفنان مع الاغنية**")
        print(str(e))
        return
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**- [freedom](t.me/xl444)**"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("- **جاري الارسال ..**")
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("خطأ ، تواصل مع مطور البوت - @rr8r9")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@app.on_message(filters.regex('^(.*) !!'))
def song232(_, message):
  text = message.text
  if '!!!' in text:
      print("Error")
  else:
    g = text.split(" ")
    query = str(g[0])
    m = message.reply("- يتم البحث الان .")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("✗ لم اجد شيئا.\n\nاعطني اسم المغني كامل.")
        print(str(e))
        return
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"**- ** [Developer](t.me/rr8r9)"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("- **جاري الارسال ..**")
        message.reply_audio(
            audio_file,
            caption=rep,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
        )
        m.delete()
    except Exception as e:
        m.edit("خطأ ، تواصل مع مطور البوت")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
