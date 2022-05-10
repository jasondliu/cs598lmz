import lzma
lzma.LZMAFile

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
import xbmcvfs

from resources.lib.modules import control
from resources.lib.modules import downloader
from resources.lib.modules import extract
from resources.lib.modules import log_utils
from resources.lib.modules import utils

try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database

addon_id = utils.addon_id
addon_name = utils.addon_name
addon_version = utils.addon_version
addon = xbmcaddon.Addon(id=addon_id)
addon_path = addon.getAddonInfo('path').decode('utf-8')
addon_profile = xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8')
addon_fanart =
