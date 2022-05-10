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

from bs4 import BeautifulSoup

# Global variables
addon = xbmcaddon.Addon()
addon_id = addon.getAddonInfo('id')
addon_name = addon.getAddonInfo('name')
addon_version = addon.getAddonInfo('version')
addon_path = addon.getAddonInfo('path').decode('utf-8')
addon_profile = addon.getAddonInfo('profile').decode('utf-8')
addon_type = addon.getAddonInfo('type').decode('utf-8')
addon_author = addon.getAddonInfo('author').decode('utf-8')
addon_changelog = addon.getAddonInfo('changelog').decode('utf-8')
addon_description = addon.getAddonInfo('description').decode('utf
