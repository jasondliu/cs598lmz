import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('disclosure.db')
import base64

# Cryptokitties
# Contract
# https://etherscan.io/address/0x06012c8cf97bead5deae237070f9587f8e7a266d
# Contract ABI
# https://etherscan.io/address/0x06012c8cf97bead5deae237070f9587f8e7a266d#code

# From https://github.com/kobigurk/ens/blob/master/ens.py
class PyENS():
    def __init__(self, sqlite_db):
        self.conn = sqlite3.connect(sqlite_db)
        self.curs = self.conn.cursor()
        self.null_addr = "0x0000000000000000000000000000000000000000"
        self.again = 0
        self.symb = threading.Thread(target=self.thread_symb_bn)
        self.symb.daemon = True
        self.symb.start()

