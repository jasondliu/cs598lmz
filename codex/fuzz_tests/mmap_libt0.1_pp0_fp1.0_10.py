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
from datetime import datetime
from datetime import timedelta
from HTMLParser import HTMLParser
from HTMLParser import HTMLParseError
from Queue import Queue
from Queue import Empty
from threading import Thread
from xml.etree import ElementTree

# Global variables
addon = xbmcaddon.Addon()
addon_id = addon.getAddonInfo('id')
addon_name = addon.getAddonInfo('name')
addon_version = addon.getAddonInfo('version')
addon_path = addon.getAddonInfo('path')
addon_profile = addon.getAddonInfo('profile')
addon_icon = addon.getAddonInfo('icon')
addon_fanart = addon.getAddonInfo('fanart')
addon_author = addon.getAddonInfo
