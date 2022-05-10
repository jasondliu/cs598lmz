import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/Users/bryan/Library/Application Support/Google/Chrome/Default/History")
# Test sqlite3.connect("/Users/bryan/Library/Application Support/Google/Chrome/Default/History").cursor().execute("select * from urls")
# Test sqlite3.connect("/Users/bryan/Library/Application Support/Google/Chrome/Default/History").cursor().execute("select * from urls").fetchall()

class Chrome(object):

    def __init__(self):
        self.lib_name = ctypes.util.find_library("libcrypto.dylib")
        self.lib = ctypes.CDLL(self.lib_name)
        self.lib.OpenSSL_add_all_algorithms()
        self.lib.OpenSSL_add_all_algorithms()

    def decrypt_string(self, encrypted_string, key):
        salt = encrypted_string[3:11]
        encrypted_data = encrypted_string[11:]
        data = self.decrypt(encrypted_data, key, salt)
        return
