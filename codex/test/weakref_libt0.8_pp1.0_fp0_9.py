import weakref
from io import BytesIO
import os
import asyncio
import html
import re
import json
from datetime import datetime, timedelta

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

from userbot import CMD_HELP, bot, BOTLOG, BOTLOG_CHATID, YOUTUBE_API_KEY, CHROME_DRIVER, GOOGLE_CHROME_BIN
from userbot.events import register


async def edrep(event):
    textx = await event.get_reply_message()
    if textx:
        reply_id = textx.id
    else:
        return
    rep_msg = await event.get_reply_message()
    if rep_msg.text:
        reply = rep_msg.text
    else:
        reply = rep_msg.ca
