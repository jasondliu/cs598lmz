import mmap
import os
import re
import sys
import time
import traceback
import urllib
import urlparse

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

from resources.lib.modules import client
from resources.lib.modules import control
from resources.lib.modules import log_utils
from resources.lib.modules import metacache
from resources.lib.modules import player
from resources.lib.modules import trakt
from resources.lib.modules import utils
from resources.lib.modules import views

sysaddon = sys.argv[0]
syshandle = int(sys.argv[1])

artPath = control.artPath()
addonFanart = control.addonFanart()
imdbCredentials = False if control.setting('imdb.user') == '' else True
traktCredentials = trakt.getTraktCredentialsInfo()
traktIndicators = trakt.getTraktIndicatorsInfo()
queueMenu = control.lang(32065).encode('utf-8')


class Movies:
   
