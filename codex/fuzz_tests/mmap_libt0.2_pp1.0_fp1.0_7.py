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
from random import randint
from random import shuffle
from resources.lib.common import *
from resources.lib.common import _addon
from resources.lib.common import _addon_id
from resources.lib.common import _addon_path
from resources.lib.common import _database_name
from resources.lib.common import _database_path
from resources.lib.common import _debugging
from resources.lib.common import _get_keyboard
from resources.lib.common import _log
from resources.lib.common import _plugin
from resources.lib.common import _plugin_id
from resources.lib.common import _plugin_path
from resources.lib.common import _plugin_url
from resources.lib.common import _set_view

