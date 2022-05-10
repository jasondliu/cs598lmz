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

# Add our resources/lib to the python path
addon_path = xbmcaddon.Addon().getAddonInfo('path')
sys.path.append(xbmc.translatePath(os.path.join(addon_path, 'resources', 'lib')))

import requests

from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Plugin Info
ADDON_ID = 'plugin.video.nhl'
REAL_SETTINGS = xbmcaddon.Addon(id=ADDON_ID)
ADDON_NAME = REAL_SETTINGS.getAddonInfo('name')
SETTINGS_LOC = REAL_SETTINGS.getAddonInfo('profile')
ADD
