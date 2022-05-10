import mmap
import os
import re
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

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from pytz import timezone

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
_handle = int(sys.argv[1])

_addon = xbmcaddon.Addon()
_addon_path = _addon.getAddonInfo('path')
_icon = _addon.getAddonInfo('icon')
_fanart = _addon.getAddonInfo('fanart')
_addonname = _addon.getAddonInfo('name')
_id = _addon.getAddonInfo('id')
_version = _addon.getAddonInfo('version')

_language = _addon.getLocalizedString
_debug = _addon.getSetting
