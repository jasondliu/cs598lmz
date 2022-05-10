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

# Set our common addon variables
__addon__ = Addon('plugin.video.youtube')
__addonid__ = __addon__.get_id()
__addonversion__ = __addon__.get_version()
__addonname__ = __addon__.get_name()
__addonpath__ = __addon__.get_path()
__addonprofile__ = __addon__.get_profile()
__addonicon__ = __addon__.get_icon()
__addonfanart__ = __addon__.get_fanart()
__addonlanguage__ = __addon__.get_language()
__addon_url__ = sys.argv[0]
__addon_handle__ = int(sys.argv[1])
__addon_queries__ = url
