import config

from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)
from HnYMusic import BOT_USERNAME, F_OWNER


def start_pannel():
        buttons = [
            [
                InlineKeyboardButton(
                    text="🔓ʜᴏᴡ ᴛᴏ ᴜꜱᴇ? ᴄᴏᴍᴍᴀɴᴅꜱ ᴍᴇɴᴜ.", callback_data="fallen_help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🌀 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ 🌀", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🥀 ʙᴏᴛ ᴏᴡɴᴇʀ 🥀", user_id=F_OWNER
                )
            ],
            [
                InlineKeyboardButton(
                    text="🇮🇳 ꜱᴜᴘᴘᴏʀᴛ 🇮🇳", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="〽️ ᴄʜᴀɴɴᴇʟ 〽️", url=config.SUPPORT_CHANNEL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🤖 ɢɪᴛ ʀᴇᴘᴏ 🤖", url="https://telegra.ph/file/2614b9f734af35d9f7d2f.jpg"
                )
            ],
        ]
        return buttons


def private_panel():
        buttons = [
            [
                InlineKeyboardButton(
                    text="🔓ʜᴏᴡ ᴛᴏ ᴜꜱᴇ? ᴄᴏᴍᴍᴀɴᴅꜱ ᴍᴇɴᴜ.", callback_data="fallen_help"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🌀 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ 🌀", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🥀 ʙᴏᴛ ᴏᴡɴᴇʀ 🥀", user_id=F_OWNER
                )
            ],
            [
                InlineKeyboardButton(
                    text="🇮🇳 ꜱᴜᴘᴘᴏʀᴛ 🇮🇳", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="〽️ ᴄʜᴀɴɴᴇʟ 〽️", url=config.SUPPORT_CHANNEL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🤖 ɢɪᴛ ʀᴇᴘᴏ 🤖", url="https://telegra.ph/file/2614b9f734af35d9f7d2f.jpg"
                )
            ],
        ]
        return buttons

