import ctypes
import ctypes.util
import threading
import sqlite3
import queue
import time
import enum

skip_months = { 2: 29, 4: 30, 9: 30, 11: 30 }

class LED_COLOR(enum.IntEnum):
  RED = 0
  GREEN = 1
  BLUE = 2

class LIGHT_STATE(enum.IntEnum):
  OFF = 0
  ON = 1
  FLASH = 2
  STROBE = 3
  FADE = 4
  SMOOTH = 5

led_color_bits = {
  LED_COLOR.RED: (1 << 0),
  LED_COLOR.GREEN: (1 << 1),
  LED_COLOR.BLUE: (1 << 2)
}

# NOTE: support tested on Raspberry Pi ZeroW only.
class rpi_matrix(threading.Thread):
  def __init__(self,
               rows_count = 16,
               columns_count = 32,
               **kwargs):
    super().__init__()

