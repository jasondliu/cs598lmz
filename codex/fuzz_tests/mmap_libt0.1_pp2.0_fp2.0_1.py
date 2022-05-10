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
__url__ = "http://code.google.com/p/plugin-video-nhl/"
__svn_url__ = "http://plugin-video-nhl.googlecode.com/svn/trunk/"
__credits__ = "XBMC TEAM, Jurialmunkey, t0mm0, Eldorado, the-one, spiff, jbeluch, jonathanbeluch, Guilouz, daskey1, mikeb"
__version__ = "1.0.0"

# Paths
BASE_PATH = xbmc.translatePath(os.path.join('special://home', '
