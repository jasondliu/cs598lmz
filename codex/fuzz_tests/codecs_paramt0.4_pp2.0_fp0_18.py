import codecs
codecs.register_error('ignore', codecs.lookup('utf8'))

import re
import os
import sys
import time
import datetime
import socket
import urllib
import urllib2
import urlparse
import logging
import logging.handlers
import traceback
import cookielib
import mimetypes
import mimetools
import tempfile
import shutil
import string
import random
import gzip
import zlib

from cStringIO import StringIO

import xbmc
import xbmcgui
import xbmcaddon

__addon__        = xbmcaddon.Addon()
__addonid__      = __addon__.getAddonInfo('id')
__addonname__    = __addon__.getAddonInfo('name')
__addonpath__    = xbmc.translatePath(__addon__.getAddonInfo('path'))
__addonprofile__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
__addonversion__ = __addon__.getAddonInfo('version')
__xbmcversion__  = x
