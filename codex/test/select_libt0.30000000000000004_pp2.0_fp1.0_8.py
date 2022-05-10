import select
import socket
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.dom.minidom

from xml.parsers.expat import ExpatError

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib.common import *
from resources.lib.utils import *

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonpath__ = __addon__.getAddonInfo('path')
__version__ = __addon__.getAddonInfo('version')
__language__ = __addon__.getLocalizedString

__profile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
