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

from resources.lib.modules import client
from resources.lib.modules import control
from resources.lib.modules import metacache
from resources.lib.modules import playcount
from resources.lib.modules import trakt
from resources.lib.modules import views
from resources.lib.modules import workers
from resources.lib.modules import youtube

try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database

try:
    import json
except:
    import simplejson as json

addon = xbmcaddon.Addon('plugin.video.venom')
addonPath = xbmc.translatePath(addon.getAddonInfo('path'))
dataPath = xbmc.translatePath(addon.getAddonInfo('profile')).decode('utf-8')
art
