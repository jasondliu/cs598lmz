import select
import socket
import sys
import time
import traceback
import urllib
import urlparse

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib.utils import log
from resources.lib.utils import notify
from resources.lib.utils import settings
from resources.lib.utils import utils
from resources.lib.utils.poutil import po

# Global variables
addon = xbmcaddon.Addon()
addon_id = addon.getAddonInfo('id')
addon_name = addon.getAddonInfo('name')
addon_version = addon.getAddonInfo('version')
addon_path = addon.getAddonInfo('path')
addon_profile = xbmc.translatePath(addon.getAddonInfo('profile'))
addon_strings = addon.getLocalizedString
addon_handle = int(sys.argv[1])
addon_url = sys.argv[0]
addon_queries = urlparse.parse_qs(sys.argv[2][1:])
addon_
