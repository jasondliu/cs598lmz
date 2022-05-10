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

# Import the common settings
from resources.lib.settings import Settings
from resources.lib.settings import log
from resources.lib.settings import os_path_join
from resources.lib.settings import os_path_split
from resources.lib.settings import os_path_splitdrive
from resources.lib.settings import os_path_splitext
from resources.lib.settings import os_path_splitunc
from resources.lib.settings import os_path_join
from resources.lib.settings import os_path_isdir
from resources.lib.settings import os_path_isfile
from resources.lib.settings import os_path_exists
from resources.lib.settings import os_remove
from resources.lib.settings import os_listdir
from resources.lib.settings import os_walk
from resources.lib.settings import os_path_
