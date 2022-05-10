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

# Addon constants
__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__addonname__ = __addon__.getAddonInfo('name')
__addonpath__ = __addon__.getAddonInfo('path').decode("utf-8")
__addonprofile__ = xbmc.translatePath(__addon__.getAddonInfo('profile')).decode("utf-8")
__addonicon__ = xbmc.translatePath(os.path.join(__addonpath__, 'icon.png'))
__addonfanart__ = xbmc.translatePath(os.path.join(__addonpath__, 'fanart.jpg'))
__addonresource__ = xbmc.
