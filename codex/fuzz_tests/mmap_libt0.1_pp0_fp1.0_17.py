import mmap
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
from resources.lib.modules import client
from resources.lib.modules import debrid
from resources.lib.modules import log_utils
from resources.lib.modules import source_utils
from resources.lib.modules import workers
from resources.lib.modules import utils

sysaddon = sys.argv[0]
syshandle = int(sys.argv[1])

class source_factory:
    def __init__(self):
        self.sources = []
        self.sourceDict = []
        self.sourceDict = self.sources_get()
        self.source_list = []
        self.source_file = control.providercacheFile
        self.hostDict = []
        self.hostprDict = []
        self.hostcapDict = []
       
