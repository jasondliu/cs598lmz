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
__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__addonversion__ = __addon__.getAddonInfo('version')
__addonpath__ = __addon__.getAddonInfo('path')
__addonprofile__ = __addon__.getAddonInfo('profile')
__addonicon__ = __addon__.getAddonInfo('icon')
__addonfanart__ = __addon__.getAddonInfo('fanart')
__addonlanguage__ = __addon__.getLocalizedString
__addon_url__ = sys.argv[0]
__addon_handle__ = int(sys.argv[1])

# Addon settings
__addon_debug__ = __addon__.
