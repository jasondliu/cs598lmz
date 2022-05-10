import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse
import xml.dom.minidom

from lxml import etree

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib import common
from resources.lib import metadata
from resources.lib import settings

_addon = xbmcaddon.Addon()
_addon_id = _addon.getAddonInfo('id')
_addon_name = _addon.getAddonInfo('name')
_addon_path = _addon.getAddonInfo('path')
_addon_version = _addon.getAddonInfo('version')
_addon_profile = xbmc.translatePath(_addon.getAddonInfo('profile'))
_addon_strings = _addon.getLocalizedString
_addon_handle = int(sys.argv[1])
_addon_url = sys.argv[0]
_addon_queries = urlparse.parse_qs(sys.argv[
