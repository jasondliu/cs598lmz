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

from addon.common.addon import Addon
from addon.common.net import Net

from metahandler import metahandlers
from metahandler import metacontainers

# Import the common settings
from settings import Settings
from settings import log
from settings import os_path_join
from settings import os_path_split
from settings import os_path_splitdrive
from settings import os_path_splitext

# Import the common run plugins
from runplugins import RunPlugin

# Import the common cache
from cache import Cache

# Import the common search
from search import Search

# Import the common download utils
from downloadutils import DownloadUtils

# Import the common resolver
from resolvers import Resolver

# Import the common context menu
from contextmenu import ContextMenu

# Import the common favorites
from
