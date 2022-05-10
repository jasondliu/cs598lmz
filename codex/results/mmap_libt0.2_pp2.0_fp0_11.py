import mmap
import os
import re
import sys
import time
import urllib
import urllib2
import urlparse

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib import common
from resources.lib import config
from resources.lib import kodi_utils
from resources.lib import kodi_vars
from resources.lib import kodi_window
from resources.lib import menu_items
from resources.lib import nav_base
from resources.lib import nav_movies
from resources.lib import nav_tv
from resources.lib import nav_utils
from resources.lib import utils
from resources.lib.addon import Addon
from resources.lib.addon import AddonSettings
from resources.lib.addon import AddonUtils
from resources.lib.addon import AddonWindow
from resources.lib.addon import AddonWindowSelect
from resources.lib.addon import AddonWindowTextViewer
from resources.lib.addon import AddonWindowXMLDialog
from resources.lib.addon import AddonXMLDialog
from resources.lib.api
