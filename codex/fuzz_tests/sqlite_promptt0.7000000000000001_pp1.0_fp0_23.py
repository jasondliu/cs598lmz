import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection().

from lib import user_config, db
from lib.user_config import UserConfig
from lib.db import DataBase

from lib.log import Log
from lib.cache import Cache
from lib.server import Server
from lib.client import Client


class TestUserConfig(unittest.TestCase):
    def setUp(self):
        pass

    def test_init(self):
        self.assertEqual(UserConfig("./tmp.config").configs, {
            "SERVER_MODE": True,
            "ENCRYPTION": True,
            "ENCRYPTION_METHOD": "aes",
            "ENCRYPTION_KEY": "12345678",
            "ENCRYPTION_IV": "12345678",
            "LOG_LEVEL": "debug",
            "LOG_PATH": "./log/",
            "LISTEN": "0.0.0.0",
            "PORT": 10086,
            "DB_PATH": "./tmp.db",
            "CACHE_PATH": "./cache.txt",
