import ctypes
import ctypes.util
import threading
import sqlite3
import uuid
import base64

try:
    import xdg.BaseDirectory
    dirname = xdg.BaseDirectory.save_data_path('AQA')
except ImportError:
    dirname = os.path.expanduser("~/.config/AQA")

from . import message


class Aqa (object):
    def __init__(self, appid):
        self.messages = Messages(appid)
        self.appid = appid

    def __del__(self):
        self.messages.finalize()

    def get_appid(self):
        return self.appid

    def get_messages(self, type="notification"):
        return self.messages.get_messages(type)

    def get_message_ids(self, type="notification"):
        return self.messages.get_message_ids(type)

def g_type_check_instance_is_a(self, type):
    return self.isinstance(type)

