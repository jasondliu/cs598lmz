import ctypes
import ctypes.util
import threading
import sqlite3
import hashlib
import subprocess
import requests
import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
import xbmcplugin

from xbmcgui import ListItem

# Version
__version__ = '0.1.1'

# KODI
try:
    __addon__ = xbmcaddon.Addon(id='plugin.video.pony')
except RuntimeError as e:
    __addon__ = xbmcaddon.Addon(id='plugin.video.pony')

# Define plugin
__url__ = sys.argv[0]
__handle__ = int(sys.argv[1])

# Database
__database__ = os.path.join(__addon__.getAddonInfo('path'), 'database', 'database.db')

# Library
__library__ = os.path.join(__addon__.getAddonInfo('path'), 'library')
__library__ = xbmc.translatePath(__library__)

# Log
__log__ = os.path.join(
