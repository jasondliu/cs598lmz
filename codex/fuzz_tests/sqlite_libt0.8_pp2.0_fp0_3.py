import ctypes
import ctypes.util
import threading
import sqlite3
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import json
import xbmcvfs
import os

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
ADDON_ICON = ADDON.getAddonInfo('icon')
ADDON_VERSION = ADDON.getAddonInfo('version')

ADDON_DATA_PATH = xbmc.translatePath("special://profile/addon_data/%s" % ADDON_ID).decode("utf-8")
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0"

DATABASE = os.path.join(ADDON_DATA_PATH, "storage.db")

# Database
def execute(query, args=(), fetch=False):
	ret = None
	try:
		conn
