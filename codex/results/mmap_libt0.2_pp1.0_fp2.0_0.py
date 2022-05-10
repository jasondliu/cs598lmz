import mmap
import os
import re
import sys
import time
import traceback

from . import __version__
from . import config
from . import constants
from . import exceptions
from . import helpers
from . import log
from . import utils
from . import xlogging

_logger = logging.getLogger(__name__)

_g_aio_ctx = None
_g_aio_ctx_lock = threading.Lock()
_g_aio_ctx_ref_count = 0
_g_aio_ctx_ref_count_lock = threading.Lock()


def _aio_ctx_ref_count_inc():
    global _g_aio_ctx_ref_count
    with _g_aio_ctx_ref_count_lock:
        _g_aio_ctx_ref_count += 1


def _aio_ctx_ref_count_dec():
    global _g_aio_ctx_ref_count
    with _g_aio_ctx_ref_count_lock:
        _g_aio_ctx
