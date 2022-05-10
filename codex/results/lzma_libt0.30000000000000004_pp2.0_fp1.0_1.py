import lzma
lzma.open

import json
import os
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

import requests

# Addon Info
ADDON_ID = 'plugin.video.hulu'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME = REAL_SETTINGS.getAddonInfo('name')
ADDON_PATH = REAL_SETTINGS.getAddonInfo('path').decode('utf-8')
ADDON_VERSION = REAL_SETTINGS.getAddonInfo('version')
ICON = REAL_SETTINGS.getAddonInfo('icon')
FANART = REAL_SETTINGS.getAddonInfo('fanart')
LANGUAGE = REAL_SETTINGS.getLocalizedString

# Plugin Info
PLUGIN_NAME = 'Hulu'
PLUGIN_ID = 'plugin.video.hulu'
PL
