import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys
import os
import re
import time
import datetime
import logging
import logging.handlers
import traceback
import threading
import Queue
import urllib
import urllib2
import urlparse
import socket
import cookielib
import json
import xml.dom.minidom
import xml.etree.ElementTree
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import xbmcvfs

from resources.lib.utils import *
from resources.lib.utils import _
from resources.lib.utils import log
from resources.lib.utils import logD
from resources.lib.utils import logE
from resources.lib.utils import logW
from resources.lib.utils import logI
from resources.lib.utils import logV
from resources.lib.utils import getAddonInfo
from resources.lib.utils import getAddonPath
from resources.lib.utils import getAddonVersion
from resources.lib.utils import getAddonSetting
from resources.lib.utils import
