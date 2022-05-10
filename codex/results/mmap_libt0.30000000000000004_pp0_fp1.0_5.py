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

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
from datetime import datetime
from datetime import timedelta
from threading import Thread
from threading import Timer
from threading import Lock
from xml.dom.minidom import parseString

__addon__        = xbmcaddon.Addon()
__addonid__      = __addon__.getAddonInfo('id')
__addonversion__ = __addon__.getAddonInfo('version')
__addonname__    = __addon__.getAddonInfo('name')
__addonpath__    = __addon__.getAddonInfo('path')
__addonprofile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__addondata__    = xbmc.translatePath(__addon
