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

# Addon info
__addon__        = xbmcaddon.Addon()
__addonid__      = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__addonname__    = __addon__.getAddonInfo('name')
__addonpath__    = __addon__.getAddonInfo('path')
__addonprofile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__icon__         = __addon__.getAddonInfo('icon')
__fanart__       = __addon__.getAddonInfo('fanart')
__language__     = __addon__.getLocalizedString

# Shared resources
BASE_RESOURCE_PATH = os.path.join(__addonpath__, "resources")
sys.path.append
