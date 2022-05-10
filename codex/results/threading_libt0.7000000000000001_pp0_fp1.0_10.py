import threading
threading.stack_size(67108864)

#regex
import re

#datetime
from datetime import datetime

#json
import json

#sqlite3
import sqlite3

#other moudels
import src.modules.moudles as moudles

#commands
import src.commands.commands as commands

#config
import src.config.config as config

#messages
import src.messages.messages as messages

#discord
import discord
from discord.ext import commands

class bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #variables
        self.bot_start_time = datetime.now()

        def get_prefix(bot, message):
            prefixes = [self.config["prefix"], f"<@!{self.user.id}> ", f"<@{self.user.id}> "]
            return commands.when_mentioned_or(*prefixes)(bot,
