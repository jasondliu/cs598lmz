import ctypes
import ctypes.util
import threading
import sqlite3
import time

from . import config
from . import utils
from . import logger

log = logger.get(__name__)

def _get_db_path():
    #~/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.ApplicationRecentDocuments/com.apple.finder.sfl
    #~/Library/Preferences/com.apple.finder.plist
    #~/Library/Preferences/com.apple.sidebarlists.plist
    #~/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentApplications.sfl
    #~/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentDocuments.sfl
    #~/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentServers.sfl
    #~/Library/Application Support/com.apple.sharedfilelist/com.apple.LSSharedFileList.RecentHosts.sfl

