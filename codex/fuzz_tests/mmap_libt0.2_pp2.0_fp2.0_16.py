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

from addon.common.addon import Addon
from addon.common.net import Net
from metahandler import metahandlers

# Addon Constants
__addon__ = Addon('plugin.video.icefilms', sys.argv)
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__addonpath__ = __addon__.getAddonInfo('path')
__lang__ = __addon__.getLocalizedString
__version__ = __addon__.getAddonInfo('version')

# Shared resources
BASE_RESOURCE_PATH = os.path.join(__addonpath__, "resources")
sys.path.append(os.path.join(BASE_RESOURCE_PATH, "lib"))

# Global Vari
