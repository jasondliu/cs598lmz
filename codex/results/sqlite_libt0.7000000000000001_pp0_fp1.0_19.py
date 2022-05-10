import ctypes
import ctypes.util
import threading
import sqlite3
import time
import sys
sys.path.append("../")
from db_api import *
from ..common.crypto import AESCipher
from ..common.util import *
from ..common.const import *

class nfc_card(object):
    def __init__(self, NfcCallBack):
        self.lib_nfc = ctypes.CDLL(ctypes.util.find_library("nfc"))
        
        self.pnd = None
        self.device = None
        self.num_device = 0
        self.context = None
        self.init_nfc()
        self.init_device()
        self.callback = NfcCallBack
        self.tmp_uid = ""
        self.tmp_data = ""
        self.tmp_pwd = ""
        self.tmp_key = ""
        self.tmp_new_pwd = ""
        self.tmp_new_key = ""
        self.tmp_algo = ""

        self.init_sqlite()

        self.card_info = {
            "uid": "",
