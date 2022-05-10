import socket
import struct
import typing
from collections import defaultdict

import discord
import psutil
from discord.ext import commands

from .utils.converters import ServerID
from .utils.paginator import Pages


class Admin(commands.Cog):
    """Administration commands"""
    def __init__(self, bot):
        self.bot = bot
    
    async def cog_check(self, ctx):
        return await self.bot.is_owner(ctx.author)
    
    @commands.command(aliases=("cogs", "load"))
    async def cog(self, ctx, *, cog: str):
        """Load a cog
        
        Cogs are Python files in the cogs package.
        """
        try:
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.send("Cog loaded")
        except Exception as e:
            await ctx.send(f"Something went wrong when loading the cog\n{type(e).__name__}: {e}")

   
