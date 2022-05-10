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

from BeautifulSoup import BeautifulSoup
from BeautifulSoup import BeautifulStoneSoup
from BeautifulSoup import SoupStrainer

from resources.lib.common import *
from resources.lib.common import log
from resources.lib.common import settings
from resources.lib.common import version
from resources.lib.common import xbmc_busy
from resources.lib.common import xbmc_notify
from resources.lib.common import xbmc_player
from resources.lib.common import xbmc_sleep
from resources.lib.common import xbmc_version
from resources.lib.common import xbmc_wait_for_video_end
from resources.lib.common import xbmc_wait_for_video_start
from resources.lib.common import xbmc_video_info
from resources.lib.common import xbmc_video_play
from
