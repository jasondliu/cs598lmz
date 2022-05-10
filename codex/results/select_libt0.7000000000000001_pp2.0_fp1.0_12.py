import selectors
import sqlite3
import time
import traceback

from typing import Optional, Type

import discord
from discord.ext import commands
from discord.ext.commands import CommandError

from cogs.utils.chat_formatting import pagify
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
from cogs.utils.context import Context

from .utils import checks, formats


class Fun:
    """Fun stuff."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/fun/settings.json")

    @commands.command(aliases=["8ball"], pass_context=True)
    async def _8ball(self, ctx: Context, *, question: str):
        """Ask 8 ball a question
        Question must end with a question mark.
        """
        if question.endswith("?") and question != "?":
            await self.bot.say("`" + random.choice(self.bot.config.eight
