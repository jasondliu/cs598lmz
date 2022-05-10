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

from resources.lib.common import *
from resources.lib.common import log
from resources.lib.common import settings
from resources.lib.common import utils
from resources.lib.common.exceptions import Error
from resources.lib.common.exceptions import PluginError
from resources.lib.common.exceptions import StreamError
from resources.lib.common.exceptions import StreamsError
from resources.lib.common.exceptions import VideoUnavailableError
from resources.lib.common.exceptions import VideoUnavailableStreamError
from resources.lib.common.exceptions import VideoUnavailableStreamsError
from resources.lib.common.exceptions import VideoUnavailableVideoError
from resources.lib.common.exceptions import VideoUnavailableVideoStreamError
from resources.lib.common.exceptions import VideoUnavailable
