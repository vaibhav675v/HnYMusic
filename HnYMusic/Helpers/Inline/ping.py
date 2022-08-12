import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ping_ig = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="sᴜᴩᴩᴏʀᴛ",
                    url=config.SUPPORT_CHAT,
                ),
                InlineKeyboardButton(
                    text="sᴏᴜʀᴄᴇ",
                    url="https://telegra.ph/file/2614b9f734af35d9f7d2f.jpg"
                )
            ]
        ]
    )
