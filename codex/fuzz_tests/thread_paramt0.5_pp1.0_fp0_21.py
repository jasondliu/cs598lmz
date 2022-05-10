import sys, threading
threading.Thread(target=lambda: None).start()
sys.modules['__main__'].__dict__.clear()
del threading, sys

# Importing everything needed for the bot
import discord
import asyncio
import traceback
import random
import time
import sys
import os
import datetime
import aiohttp
import json
import requests
import io
import functools
import re
import youtube_dl
import subprocess
import inspect
import token
import pymongo
import mongo_link
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import find
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from discord import opus
from discord.utils import get
from discord.utils import find
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions
from discord.ext.commands import CommandNotFound
from discord.ext.commands import CommandOnCooldown
from discord.ext.commands import NotOwner
from discord.ext.commands import errors
from discord.ext.commands import Bot
