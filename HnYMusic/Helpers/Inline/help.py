from HnYMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


help_panel = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ",
                    callback_data="help_callback ADMIN",
                ),
                    InlineKeyboardButton(
                    text="ᴩʟᴀʏ ᴄᴏᴍᴍᴀɴᴅꜱ",
                    callback_data="help_callback PLAY",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ",
                    callback_data="help_callback TOOLS",
                ),
                    InlineKeyboardButton(
                    text="ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ",
                    callback_data="help_callback AUTH",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ꜱᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅꜱ",
                    callback_data="help_callback OWNER",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="ʙᴀᴄᴋ",
                    callback_data=f"fallen_home",
                ),
                InlineKeyboardButton(
                    text="ᴄʟᴏsᴇ",
                    callback_data=f"close"
                ),
            ]
        ]
    )


help_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ʙᴀᴄᴋ",
                    callback_data=f"fallen_help",
                ),
                InlineKeyboardButton(
                    text="ᴄʟᴏsᴇ",
                    callback_data=f"close"
                )
            ]
        ]
    )
