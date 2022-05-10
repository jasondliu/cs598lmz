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

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from threading import Thread
from threading import Timer

# Addon
__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonpath__ = xbmc.translatePath(__addon__.getAddonInfo('path'))
__lang__ = __addon__.getLocalizedString
__version__ = __addon__.getAddonInfo('version')

# Paths
BASE_RESOURCE_PATH = xbmc.translatePath(os.path.join(__addonpath__, 'resources
