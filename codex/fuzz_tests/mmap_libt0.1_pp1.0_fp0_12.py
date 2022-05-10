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
from resources.lib.modules import metacache
from resources.lib.modules import playcount
from resources.lib.modules import trakt
from resources.lib.modules import views
from resources.lib.modules import workers
from resources.lib.modules import youtube
from resources.lib.modules import utils

sysaddon = sys.argv[0] ; syshandle = int(sys.argv[1])

class navigator:
    def __init__(self):
        self.count = 0
        self.queue = workers.Thread(self.run)
        self.queue.start()

        self.meta = []
        self.all_meta = []
        self.video_type = None
        self.next_page = 0
        self.re_me = 'var\s
