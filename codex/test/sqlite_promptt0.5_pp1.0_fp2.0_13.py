import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import sys
import os
import time
import subprocess
import traceback

import xbmc
import xbmcaddon

from modules.utils import local_string as ls

try:
    from sqlalchemy.orm import sessionmaker
except:
    xbmc.log('script.module.sqlalchemy is not installed', xbmc.LOGERROR)
    xbmcgui.Dialog().ok(ls(32700), ls(32701), ls(32702))
    raise

from modules.nav_utils import build_url, set_property, get_property, close_all_dialog

addon_id = 'script.module.opensubtitles'
addon = xbmcaddon.Addon(addon_id)
profile_dir = xbmc.translatePath(addon.getAddonInfo('profile'))
opensubtitles_db = os.path.join(profile_dir, 'subtitles.db')

