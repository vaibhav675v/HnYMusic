import config
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)

from HnYMusic import db_mem


def primary_markup(videoid, user_id):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(text="▶️ʀᴇꜱᴜᴍᴇ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸ᴘᴀᴜꜱᴇ", callback_data=f"pausecb"),
        ],
        [
            InlineKeyboardButton(text="⏭ꜱᴋɪᴘ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹ᴇɴᴅ", callback_data=f"stopcb"),
        ],
        [
            
            InlineKeyboardButton(text="🗑ᴄʟᴏsᴇ", callback_data=f"close"),
        ],
    ]
    return buttons


audio_markup = InlineKeyboardMarkup(
    [
       [
            InlineKeyboardButton(text="▶️ʀᴇꜱᴜᴍᴇ", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸ᴘᴀᴜꜱᴇ", callback_data=f"pausecb"),
        ],
        [
            InlineKeyboardButton(text="⏭ꜱᴋɪᴘ", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹ᴇɴᴅ", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton("🗑ᴄʟᴏsᴇ", callback_data="close")],
    ]
)


close_key = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🗑ᴄʟᴏsᴇ", callback_data="close")],
    ]
)
