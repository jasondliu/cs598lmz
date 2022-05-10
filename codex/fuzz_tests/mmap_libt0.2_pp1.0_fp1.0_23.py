import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urllib2
import urlparse

from xml.dom import minidom

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib.common import *
from resources.lib.common import log
from resources.lib.common import settings
from resources.lib.common import utils
from resources.lib.common import xbmc_player
from resources.lib.common.exceptions import *
from resources.lib.common.utils import *
from resources.lib.common.utils import get_url
from resources.lib.common.utils import get_url_with_retry
from resources.lib.common.utils import get_url_with_retry_with_auth
from resources.lib.common.utils import get_url_with_retry_with_auth_with_proxy
from resources.lib.common.utils import get_url_with_retry_with_proxy
from resources.lib.common.utils import get_url_with
