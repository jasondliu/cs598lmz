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
from dateutil import parser
from dateutil.tz import gettz
from dateutil.tz import tzlocal
from dateutil.tz import tzutc
from dateutil.tz import tzoffset

from resources.lib.modules import control
from resources.lib.modules import log_utils
from resources.lib.modules import utils

try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database

addon_id = 'plugin.video.theroyalwe'
addon = xbmcaddon.Addon(addon_id)
addon_name = addon.getAddonInfo('name')
addon_version = addon.getAddonInfo('version')
addon_strings = addon.get
