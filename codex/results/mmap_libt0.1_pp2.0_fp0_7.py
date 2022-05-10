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

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from threading import Thread

# Addon info
__addon__ = xbmcaddon.Addon()
__addonid__ = __addon__.getAddonInfo('id')
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonpath__ = __addon__.getAddonInfo('path')
__addonversion__ = __addon__.getAddonInfo('version')
__addonprofile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__addonlanguage__ = __addon__.getLocalizedString
__addonfanart__ = __addon__.getAddonInfo('fanart')
__addonauthor__ = __addon__
