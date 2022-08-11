import os
import time
import config
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import Message

from HnYMusic.Helpers.Inline import ping_ig
from HnYMusic.Helpers.Ping import get_readable_time
from HnYMusic import BOT_USERNAME, BOT_NAME, app, StartTime


__MODULE__ = "Pɪɴɢ"
__HELP__ = """

/ping or /alive
» ᴄʜᴇᴄᴋ ɪғ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ. [ɪғ ᴀʟɪᴠᴇ sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.]
"""


async def fallen_ping():
    uptime = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    fallen = f"""
ᴜᴩᴛɪᴍᴇ : {get_readable_time((uptime))}
ᴄᴩᴜ : {cpu}%
ʀᴀᴍ : {mem}%
ᴅɪsᴋ : {disk}%"""
    return fallen

@app.on_message(filters.command(["ping", "alive", f"ping@{BOT_USERNAME}"]))
async def ping(_, message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG,
        caption="**» ᴩɪɴɢɪɴɢ ʙᴀʙʏ...**",
    )
    hehe = await fallen_ping()
    start = datetime.now()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await hmm.edit_text(
        f"**» ᴩᴏɴɢ ʙᴀʙʏ !**\n`☁ {resp}`ᴍs\n\n<b><u>{BOT_NAME} sʏsᴛᴇᴍ sᴛᴀᴛs :</u></b>{hehe}",
        reply_markup=ping_ig,
    )
