import ctypes
import ctypes.util
import threading
import sqlite3
import os

class Client:
    def __init__(self):
        self.connected = False
        self.retries = 0
        self.db = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.sqlite3'), check_same_thread=False)
        self.cursor = self.db.cursor()
        self.token = self.cursor.execute('SELECT token FROM secret').fetchone()[0]
        self.client = discord.Client()
        self.create_tables()
        self.init_handlers()

    def init_handlers(self):
        @self.client.event
        async def on_ready():
            self.connected = True

        @self.client.event
        async def on_message(message):
            if message.author.bot:
                return
            if message.channel.name == 'commands':
                if message.content.startswith('!add'):
                    content = message.content.split(' ')
                    if not content[1].isd
