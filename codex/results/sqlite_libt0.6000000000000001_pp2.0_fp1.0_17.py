import ctypes
import ctypes.util
import threading
import sqlite3
import time

class SpheroController(threading.Thread):
  def __init__(self, bot_id, bot_name, bot_mac, bot_color, callback):
    threading.Thread.__init__(self)
    self.bot_id = bot_id
    self.bot_name = bot_name
    self.bot_mac = bot_mac
    self.bot_color = bot_color
    self.callback = callback

    # load library
    self.lib = ctypes.CDLL(ctypes.util.find_library('sphero'))
    self.lib.sphero_init()

    # create device
    self.dev = self.lib.sphero_create()
    self.lib.sphero_set_callback(self.dev, self.callback)
    self.lib.sphero_set_option(self.dev, 0x20, 1)

    # connect
    if self.lib.sphero_connect(self.dev, self.bot_mac) != 0:
      raise Exception('Could not connect')

    # enable data streaming
