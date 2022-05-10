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
__addonauthor__ = __addon__.getAddonInfo('author')
__addonurl__ = __addon__.getAddonInfo('url')
__addonlicense__ = __addon__.getAddonInfo('license')
__addonchangelog__ = __addon
