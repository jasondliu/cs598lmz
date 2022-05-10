import ctypes
import ctypes.util
import threading
import sqlite3

from collections import OrderedDict
from contextlib import contextmanager
from inotify_simple import INotify, flags
from event_handler import BaseEventHandler

from paun import utils
from paun.event_handler import PrintEventHandler, SqliteEventHandler


def get_inotify_handle(version='0.2.4'):
    """
    Try to load inotify_simple.  If not present, try to download it.
    Otherwise the app won't start
    """
    try:
        from inotify_simple import INotify, flags
    except ImportError:
        from pypi.pypi import Pip
        from utils.url_utils import download_file
        
        pipi = Pip()
        download_path = download_file(pipi.get_download_url('inotify_simple', version), '~')
        pipi.install_file(download_path)
        
        import inotify_simple
        return inotify_simple.INotify()
    else:
        return INotify()
