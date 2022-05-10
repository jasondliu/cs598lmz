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
import xbmcvfs

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

try:
    from resources.lib.modules import xbmcvfs
except:
    import xbmcvfs

try:
    from resources.lib.modules import control
    control.enableDirect()
except:
    pass

sysaddon = sys.argv[0]

