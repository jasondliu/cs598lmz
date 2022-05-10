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

from resources.lib.modules import cache
from resources.lib.modules import client
from resources.lib.modules import control
from resources.lib.modules import debrid
from resources.lib.modules import log_utils
from resources.lib.modules import metacache
from resources.lib.modules import playcount
from resources.lib.modules import players
from resources.lib.modules import rd_check
from resources.lib.modules import trakt
from resources.lib.modules import utils
from resources.lib.modules import views
from resources.lib.modules import workers

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1])

class tvshows:
    def __init__(self):
        self.list = []

        self.imdb_link = 'http://www.imdb.
