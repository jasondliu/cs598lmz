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

# Global Variables
addon = xbmcaddon.Addon()
addonID = addon.getAddonInfo('id')
addonName = addon.getAddonInfo('name')
addonVersion = addon.getAddonInfo('version')
addonPath = addon.getAddonInfo('path')
addonProfile = addon.getAddonInfo('profile')
addonIcon = addon.getAddonInfo('icon')
addonFanart = addon.getAddonInfo('fanart')
addonLanguage = addon.getLocalizedString
addonDescription = addon.getAddonInfo('description')
addonAuthor = addon.getAddonInfo('author')
addonSource = addon.getAddonInfo('source')
addonWebsite = addon.getAddonInfo('website')
addonEmail = addon.getAdd
