#
# Copyright (C) 2023-2024 by YukkiOwner@Github, < https://github.com/YukkiOwner >.
#
# This file is part of < https://github.com/YukkiOwner/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YukkiOwner/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause Stream",
            description=f"ايقاف تشغيل التدفق الصوتي مؤقتا .",
            thumb_url="https://telegra.ph/file/c0a1c789def7b93f13745.png",
            input_message_content=InputTextMessageContent("مؤقتا"),
        ),
        InlineQueryResultArticle(
            title="Resume Stream",
            description=f"استمرار تشغيل التدفق الصوتي بأستمرار .",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("استمر"),
        ),
        InlineQueryResultArticle(
            title="Mute Stream",
            description=f"كتم صوت تدفق حساب المساعد مؤقتا .",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("كتم"),
        ),
        InlineQueryResultArticle(
            title="Unmute Stream",
            description=f"رفع الكتم الموجود على حساب المساعد .",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("رفع"),
        ),
        InlineQueryResultArticle(
            title="Skip Stream",
            description=f"لتخطي ملف صوتي من قائمة التشغيل . ",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("سكب"),
        ),
        InlineQueryResultArticle(
            title="End Stream",
            description="ايقاف تشغيل التدفق الصوتي في الاتصال .",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("كافي"),
        ),
        InlineQueryResultArticle(
            title="Shuffle Stream",
            description="تلقائي تفعيل وضع تشغيل تلقائي من الطابور .",
            thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
            input_message_content=InputTextMessageContent("تلقائي"),
        ),
        InlineQueryResultArticle(
            title="Seek Stream",
            description="اكتب تقديم والمدة لتقديم الملف الصوتي .",
            thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
            input_message_content=InputTextMessageContent("تقديم 10"),
        ),
        InlineQueryResultArticle(
            title="Loop Stream",
            description="اكتب تكرار مع العدد لتكرار الملف الصوتي .",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("تكرار 3"),
        ),
    ]
)
