#
# Copyright (C) 2023-2024 by YukkiOwner@Github, < https://github.com/YukkiOwner >.
#
# This file is part of < https://github.com/YukkiOwner/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YukkiOwner/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

import sys

from pyrogram import Client
from pyrogram.enums import ChatMemberStatus

from pyrogram.types import BotCommand

import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            name="YukkiMusicBot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "- تم تشغيل البوت ."
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        if config.SET_CMDS == str(False):
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("شغل", "بالرد على ملف صوتي او إعطاء شي للبحث"),
                        BotCommand("سكب", "لتخطي ملف صوتي من قائمة التشغيل"),
                        BotCommand("مؤقتا", "ايقاف تشغيل التدفق الصوتي مؤقتا "),
                        BotCommand("استمر", "استمرار تشغيل التدفق الصوتي بأستمرار"),
                        BotCommand("كتم", "كتم صوت تدفق حساب المساعد مؤقتا"),
                        BotCommand("رفع", "رفع الكتم الموجود على حساب المساعد"),
                        BotCommand("كافي", "ايقاف تشغيل التدفق الصوتي في الاتصال"),
                        BotCommand("تلقائي", "تفعيل وضع تشغيل تلقائي من الطابور"),
                        BotCommand("3 تكرار", "اكتب تكرار مع العدد لتكرار الملف الصوتي"),
                        BotCommand("تقديم 10", "اكتب تقديم والمدة لتقديم الملف الصوتي"),
                        BotCommand("يوت", "لبحث وتنزيل ملف صوتي من اليوتيوب"),
                        
                        ]
                    )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Please promote Bot as Admin in Logger Group"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
