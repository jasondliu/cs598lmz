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

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup

__addon__       = xbmcaddon.Addon()
__addonid__     = __addon__.getAddonInfo('id')
__addonname__   = __addon__.getAddonInfo('name')
__author__      = __addon__.getAddonInfo('author')
__version__     = __addon__.getAddonInfo('version')
__language__    = __addon__.getLocalizedString

__cwd__         = xbmc.translatePath( __addon__.getAddonInfo('path') ).decode("utf-8")
__profile__     = xbmc.translatePath( __addon__.getAddonInfo('profile') ).decode("utf-8")
__resource__    = xbmc.translatePath(
