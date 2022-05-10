import ctypes
import ctypes.util
import threading
import sqlite3
import time
import tkinter
import tkinter.ttk
import tkinter.filedialog

# i18n
import gettext
gettext.textdomain('youtube-dl-gui')
_ = gettext.gettext

# external modules
import youtube_dl
import youtube_dl.utils
import youtube_dl.hooks
import youtube_dl.version

# local modules
import ui
import util

# windows only
if os.name == 'nt':
    import win32api
    import win32con
    import win32gui_struct
    import ctypes.wintypes
    import comtypes.client

# cross platform support
import posix_ipc
import psutil
import termios
import tty

# python 2/3
py3 = sys.version_info >= (3, 0)
if py3:
    from urllib.parse import urlparse, unquote
    from urllib.request import urlopen
    from tkinter import font as tkFont
else:
    from urlparse import urlparse
    from ur
