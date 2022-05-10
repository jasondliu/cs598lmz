import select
import socket
import sys
import thread
import time
import traceback
import urllib
import urllib2
import urlparse

import xbmc
import xbmcaddon
import xbmcgui

__addon__ = xbmcaddon.Addon()
__cwd__ = __addon__.getAddonInfo('path')
__resource__ = xbmc.translatePath(os.path.join(__cwd__, 'resources'))
__lib__ = xbmc.translatePath(os.path.join(__resource__, 'lib'))

sys.path.append(__resource__)
sys.path.append(__lib__)
