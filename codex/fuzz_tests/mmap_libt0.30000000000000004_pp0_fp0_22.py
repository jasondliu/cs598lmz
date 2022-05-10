import mmap
import os
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

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from threading import Thread
from threading import Timer

from resources.lib import utils
from resources.lib.addon.parser import try_int
from resources.lib.addon.plugin import viewitems
from resources.lib.addon.plugin import viewmodes
from resources.lib.addon.window import get_property
from resources.lib.addon.window import set_property
from resources.lib.api import Api
from resources.lib.api import ApiError
from resources.lib.api import ApiService
from resources.lib.api.exceptions import ApiError
from resources.lib.api.items import ApiLive
from resources.lib.api.items import ApiProgram
from resources.lib.api.items import ApiRecording
from resources.lib.api.
