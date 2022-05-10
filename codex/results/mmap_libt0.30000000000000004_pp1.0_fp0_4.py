import mmap
import os
import re
import sys
import time
import urllib

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib.common import *
from resources.lib.common import log
from resources.lib.common import settings
from resources.lib.common import utils
from resources.lib.common.exceptions import Error
from resources.lib.common.exceptions import InputStreamError
from resources.lib.common.exceptions import PluginError
from resources.lib.common.exceptions import StreamError
from resources.lib.common.exceptions import StreamsError
from resources.lib.common.exceptions import VideoUnavailable
from resources.lib.common.exceptions import WebsiteParsingError
from resources.lib.modules import cache
from resources.lib.modules import client
from resources.lib.modules import control
from resources.lib.modules import debrid
from resources.lib.modules import log_utils
from resources.lib.modules import metacache
from resources.lib.modules import player
from resources.lib.modules import providers
from resources
