import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time
import subprocess
import shutil
import re
import json
import logging
import tempfile
import urllib
import urllib2
import hashlib
import traceback

from optparse import OptionParser
from collections import defaultdict

import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs

from resources.lib.utils import *
from resources.lib.utils import log
from resources.lib.utils import get_platform
from resources.lib.utils import get_temp_dir
from resources.lib.utils import get_data_dir
from resources.lib.utils import get_cache_dir
from resources.lib.utils import get_addon_dir
from resources.lib.utils import get_addon_info
from resources.lib.utils import get_addon_version
from resources.lib.utils import get_addon_profile
from resources.lib.utils import get_kodi_version
from resources.lib.utils import get_kodi_
