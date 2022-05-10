import select
import socket
import sys
import thread
import time
import traceback
import urllib
import urllib2
import urlparse

import xbmc
import xbmcaddon
import xbmcgui

__addon__ = xbmcaddon.Addon()
__cwd__ = __addon__.getAddonInfo('path')
__resource__ = xbmc.translatePath(os.path.join(__cwd__, 'resources'))
__lib__ = xbmc.translatePath(os.path.join(__resource__, 'lib'))

sys.path.append(__resource__)
sys.path.append(__lib__)

from simplejson import loads
from socket import gethostbyname, gaierror

from utils import log, notify, get_setting, set_setting, get_string, \
    get_version, get_platform, get_ipaddress, get_macaddress, \
    get_netmask, get_gateway, get_dns_servers, get_country, \
    get_kodi_json,
