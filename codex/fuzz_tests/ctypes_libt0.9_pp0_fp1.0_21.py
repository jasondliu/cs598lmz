import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('CS.pygame')

# とりあえずインポート
import random
import datetime
import discord
import asyncio
import os
import pygame
import time
import sys
import traceback
import pprint
import subprocess

# クライアント作成
client = discord.Client()

# サーバーからの入力を受け取ったら
# printくらいにしかなにもしません
@client.event
async def on_message(message):
	if message.author.bot:
		return
	
	msg = None
	if message.content.startswith('音を') and 'やめて' in message.content:
		msg = '音はおやめになりました'
		stopbgm()
		pygame.mixer.stop()
	elif message.content.startswith('
