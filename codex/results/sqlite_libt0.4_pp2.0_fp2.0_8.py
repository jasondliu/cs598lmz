import ctypes
import ctypes.util
import threading
import sqlite3
import time
import os
import sys
import re
import struct

class Mumble:
    def __init__(self, host, port, nickname, password, channel):
        self.host = host
        self.port = port
        self.nickname = nickname
        self.password = password
        self.channel = channel
        self.connected = False
        self.thread = None
        self.mumble = None
        self.mumble_user = None
        self.mumble_channel = None
        self.mumble_channel_id = None
        self.mumble_channel_name = None
        self.mumble_channel_description = None
        self.mumble_channel_position = None
        self.mumble_channel_temporary = None
        self.mumble_channel_links = None
        self.mumble_channel_links_add = None
        self.mumble_channel_links_remove = None
        self.mumble_channel_links_count = None
        self.mumble_channel_links_channel_id = None
        self.mumble
