import mmap
import os
import re
import subprocess
import sys
import time
import traceback
import urllib
import urlparse

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib.modules.common import Addon, clean_file_name, clean_title, control, get_params, set_view, log, error_log, notify, set_cookies, translation
from resources.lib.modules import client
from resources.lib.modules import cache
from resources.lib.modules import metacache
from resources.lib.modules import workers
from resources.lib.modules import views

try: from sqlite3 import dbapi2 as database
except: from pysqlite2 import dbapi2 as database

addon_id = xbmcaddon.Addon().getAddonInfo('id')
addon_name = xbmcaddon.Addon().getAddonInfo('name')
addon_icon = xbmcaddon.Addon().getAddonInfo('icon')
addon_fanart = xbmcaddon.Addon().getAddon
