import socket
import sys
import threading
import time
import traceback
import urllib
from xml.dom import minidom
from xml.parsers.expat import ExpatError

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib.utils import *

__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__addonname__ = __addon__.getAddonInfo('name')
__addonpath__ = __addon__.getAddonInfo('path')
__addonprofile__ = __addon__.getAddonInfo('profile')
__addonicon__ = __addon__.getAddonInfo('icon')
__addonfanart__ = __addon__.getAddonInfo('fanart')
__addonlanguage__ = __addon__.getLocalizedString
__addonstrings__ = __addon__.getLocalizedString
__addon_url__ = sys.argv[0]
