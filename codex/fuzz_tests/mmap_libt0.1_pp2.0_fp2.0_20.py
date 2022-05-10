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

from resources.lib.modules import control
from resources.lib.modules import client
from resources.lib.modules import debrid
from resources.lib.modules import log_utils
from resources.lib.modules import source_utils
from resources.lib.modules import workers
from resources.lib.modules import utils

try:
    from sqlite3 import dbapi2 as database
except:
    from pysqlite2 import dbapi2 as database

try:
    import resolveurl
except:
    pass

try:
    import urlresolver
except:
    pass

try:
    from resources.lib.modules import trakt
except:
    pass

try:
    from resources.lib.modules import tmdbsimple as tmdb
except:
    pass

try:
    from resources.lib.modules
