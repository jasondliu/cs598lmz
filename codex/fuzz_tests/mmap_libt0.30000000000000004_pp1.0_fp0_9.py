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
from datetime import datetime, timedelta
from threading import Thread
from xml.dom.minidom import parseString

__addon__       = xbmcaddon.Addon()
__addonid__     = __addon__.getAddonInfo('id')
__addonversion__= __addon__.getAddonInfo('version')
__addonname__   = __addon__.getAddonInfo('name')
__addonpath__   = __addon__.getAddonInfo('path')
__addonprofile__= xbmc.translatePath(__addon__.getAddonInfo('profile'))
__localize__    = __addon__.getLocalizedString

__xbmcversion__ =  xbmc.getInfoLabel( "System.BuildVersion" ).split
