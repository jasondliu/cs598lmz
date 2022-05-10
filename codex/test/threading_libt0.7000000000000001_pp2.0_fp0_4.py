import threading
threading._DummyThread._Thread__stop = lambda x: 42
import urllib
import urllib2
import urlparse
import re
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import datetime
import time
import os
import cPickle
import shutil
import cookielib
import hashlib
import unicodedata
from bs4 import BeautifulSoup
import json
import base64
import SocketServer
import BaseHTTPServer

__addon__ = xbmcaddon.Addon()
__author__     = __addon__.getAddonInfo('author')
__scriptid__   = __addon__.getAddonInfo('id')
__scriptname__ = __addon__.getAddonInfo('name')
__cwd__        = __addon__.getAddonInfo('path')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

