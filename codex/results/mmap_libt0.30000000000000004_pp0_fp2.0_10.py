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

# Import the common settings
from resources.lib.settings import Settings
from resources.lib.settings import log
from resources.lib.settings import os_path_join
from resources.lib.settings import os_path_split
from resources.lib.settings import os_path_splitext

# Import the common run plugin
from resources.lib.runplugin import RunPlugin

# Import the common cache
from resources.lib.cache import Cache

# Import the common search
from resources.lib.search import Search

# Import the common downloader
from resources.lib.downloader import Downloader

# Import the common progress dialog
from resources.lib.progress import Progress

# Import the common resolver
from resources.lib.resolver import Resolver

# Import the common resolver
from resources.lib.youtube import YouTube

# Import the common resolver
from resources.
