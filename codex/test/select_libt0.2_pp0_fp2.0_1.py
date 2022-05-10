import select
import socket
import sys
import threading
import time
import traceback
import urllib
import urllib2
import urlparse
import uuid

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib.api import API
from resources.lib.api import APIError
from resources.lib.api import APIErrorAuth
from resources.lib.api import APIErrorNotFound
from resources.lib.api import APIErrorTimeout
from resources.lib.api import APIErrorUnknown
from resources.lib.api import APIErrorUnsupported
from resources.lib.api import APIErrorVideoUnavailable
from resources.lib.api import APIErrorVideoUnsupported
from resources.lib.api import APIErrorVideoUnsupportedDRM
from resources.lib.api import APIErrorVideoUnsupportedGeo
from resources.lib.api import APIErrorVideoUnsupportedLive
from resources.lib.api import APIErrorVideoUnsupportedSubtitle
