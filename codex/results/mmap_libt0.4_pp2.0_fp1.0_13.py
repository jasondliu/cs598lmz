import mmap
import os
import re
import subprocess
import sys
import time
import win32api
import win32con
import win32gui
import win32process
import win32ui
import win32ui
from PIL import Image
from PIL import ImageChops
from PIL import ImageEnhance
from PIL import ImageFilter
from PIL import ImageGrab
from PIL import ImageOps
from PIL import ImageStat
from PIL import ImageWin
from ctypes import *
from ctypes.wintypes import *
from datetime import datetime
from threading import Thread
from time import sleep

# ======================================================================================================================
# ======================================================  Global  ======================================================
# ======================================================================================================================

# -----------------------------
# ----------  Enum  ----------
# -----------------------------
class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

# -----------------------------
# ----------  Log  -----------
# -----------------------------
class Log:
    def __init__(self):
        self.
