import codecs
# Test codecs.register_error('my_ignore', my_ignore)

import os
import datetime
import time
import sys
import logging
import gzip
import shutil
import stat
import hashlib
import string
import re
import urllib
import urllib2
import json
import xbmc
import xbmcaddon
import xbmcvfs
import xbmcgui
import xbmcplugin
import xbmcgui
import xbmcaddon
from traceback import print_exc
from xml.dom import minidom
from xml.dom.minidom import Node
import unicodedata
import random
from xml.sax.saxutils import escape

# global variables
ADDON = xbmcaddon.Addon(id = 'script.metadataandart.importer')
LANGUAGE = ADDON.getLocalizedString
ADDON_ID = ADDON.getAddonInfo("id")
ADDON_VERSION = ADDON.getAddonInfo("version")
ADDON_PATH = ADDON.getAddonInfo("path").decode("utf-8")
ADDON_DATA_PATH =
