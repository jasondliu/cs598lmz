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

# Global variables
__plugin__ = "plugin.video.nhl"
__author__ = "jurialmunkey"
__url__ = "http://code.google.com/p/plugin-nhl/"
__svn_url__ = "http://plugin-nhl.googlecode.com/svn/trunk/"
__credits__ = "XBMC TEAM, http://xbmc.org/"
__version__ = "1.0.0"

# Paths
BASE_PATH = xbmc.translatePath(os.path.join('special://home', 'addons', __plugin__))
MEDIA_PATH = os.path.join(BASE_PATH, 'resources', 'media')

# Settings
__settings__ = xbmc
