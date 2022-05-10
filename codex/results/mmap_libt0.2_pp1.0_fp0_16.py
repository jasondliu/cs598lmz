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

from resources.lib.modules import control
from resources.lib.modules import client
from resources.lib.modules import debrid
from resources.lib.modules import log_utils
from resources.lib.modules import source_utils
from resources.lib.modules import workers
from resources.lib.modules import utils

sysaddon = sys.argv[0]
syshandle = int(sys.argv[1])

class source:
    def __init__(self):
        self.priority = 1
        self.language = ['en']
        self.domains = ['www.torrentdownloads.me']
        self.base_link = 'https://www.torrentdownloads.me'
        self.search_link = '/search/?search=%s&new=1&x=0&y=0'
        self.min_seeders = int
