import ctypes
import ctypes.util
import threading
import sqlite3
import re

from telegram import Message, Chat, Update, Bot, MessageEntity
from telegram.ext import CommandHandler, run_async, Filters

from hitsuki import dispatcher, LOGGER, SUDO_USERS, SUPPORT_USERS, WHITELIST_USERS, OWNER_ID
from hitsuki.__main__ import STATS, USER_INFO, TOKEN
from hitsuki.modules.disable import DisableAbleCommandHandler
from hitsuki.modules.helper_funcs.extraction import extract_user

if not os.path.isfile("hitsuki/__main__.py"):
    SUDO_USERS.append(OWNER_ID)

if TOKEN == "TOKENHERE":
    raise ValueError("Your Telegram API TOKEN is missing! Please see the README and the inline comments in the "
                     "__main__.py file to learn how to get a token from the Telegram API, then retry the bot.")

if not os.path.isdir('./stepik'):
    os.makedirs('./stepik')
