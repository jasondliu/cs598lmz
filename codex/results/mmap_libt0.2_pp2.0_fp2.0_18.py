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

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
from dateutil import parser
from dateutil.tz import gettz
from dateutil.tz import tzlocal
from dateutil.tz import tzutc
from dateutil.tz import tzwinlocal
from dateutil.tz import tzwinutc

from resources.lib.common import *
from resources.lib.common import _addon
from resources.lib.common import _addon_path
from resources.lib.common import _database_path
from resources.lib.common import _debugging
from resources.lib.common import _date
from resources.lib.common import _http
from resources.lib.common import _image_path
from resources.lib.common import _image_settings
from resources.lib.common import _json
from resources.lib.common import _
