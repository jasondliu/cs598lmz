import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
import zipfile

from . import util
from . import version
from . import xlogging

_logger = xlogging.getLogger(__name__)

_g_aio_cache_dir = None
_g_aio_cache_dir_lock = threading.Lock()


def _get_aio_cache_dir():
    global _g_aio_cache_dir
    if _g_aio_cache_dir is None:
        with _g_aio_cache_dir_lock:
            if _g_aio_cache_dir is None:
                _g_aio_cache_dir = tempfile.mkdtemp(prefix='aio_cache_')
    return _g_aio_cache_dir


def _get_aio_cache_file(name):
    return os.path.join(_get_aio_cache_dir(), name)


def _get_aio_cache_file
