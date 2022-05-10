import ctypes
import ctypes.util
import threading
import sqlite3
from sqlite3 import Error

from message import Message
import config


class Bot(threading.Thread):
    def __init__(self, const_path, group_name):
        threading.Thread.__init__(self)
        self.daemon = False
        self.path = const_path
        self.group_name = group_name

    def run(self):
        self.create_tables()
        self.listen_messages()

    def create_tables(self):
        groups_table_creation = """CREATE TABLE IF NOT EXISTS groups (
                                       name text NOT NULL
                                   );"""
        messages_table_creation = """CREATE TABLE IF NOT EXISTS messages (
                                        name text NOT NULL,
                                        timestamp text NOT NULL,
                                        message text NOT NULL,
                                        user_name text NOT NULL
                                    );"""
        try:
            conn = sqlite3.connect(self.path + 'database/' + self.group_name)
            c = conn.cursor()
            c.execute(groups_table
