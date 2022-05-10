import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

import pl.robwork.libudev as udev

import z3c.autoinclude.plugin

SIO_RCVALL = 0x98000001

import pyxhook

def klog(e):
    print(e)

before_string = ""
class KeyBoardHooker(pyxhook.HookManager): 
    def __init__(self, conn): 
        self.conn = conn
        self.last_t = time.time()
        pyxhook.HookManager.__init__(self)
        self.keypress_event = threading.Event()
        self.to_key_down = {}
        
        self.Mask = 0
        self.MaskCtrl = 1
        self.MaskShift = 1 << 1
        self.MaskAlt = 1 << 2
        self.MaskWin = 1 << 3

        self.key_buffer = []

        self.event_hooker()
        self.hook_keyboard()
        self.start()

    def count_parttern(self, string, pattern, gap
