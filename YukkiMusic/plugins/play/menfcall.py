from pyrogram import filters, Client
from YukkiMusic import app
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError,AlreadyJoinedError)

@app.on_message(filters.regex("^الصاعدين$"))
async def strcall(client, message):
    assistant = await group_assistant(Yukki,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"), stream_type=StreamType().pulse_stream)
        text="- الصاعدين بالأتصال :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يمسلت 🗣"
            else:
                mut="ساكت 🔕"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
        await asyncio.sleep(7)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"- ماكو شي مشتغل")
    except TelegramServerError:
        await message.reply(f"- حدث خطا .")
    except AlreadyJoinedError:
        text="- الصاعدين :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="يمسلت 🗣"
            else:
                mut="ساكت 🔕"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}➤{user.mention}➤{mut}\n"
        text += f"\nعددهم : {len(participants)}\n✔️"    
        await message.reply(f"{text}")
