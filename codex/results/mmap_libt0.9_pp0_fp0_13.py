import mmap
import os
import pickle
import re
import sys
import threading
import warnings
from subprocess import check_output, CalledProcessError
from typing import Dict, List, Optional, cast

from . import __version__, which
from .errors import UserError
from .logger import log_to_client
from .models import Diagnostic, SEVERITY
from .paths import LOCAL_INSTALL_DIR, LOCAL_CONFIG_PATH

logger = logging.getLogger(__name__)

SEVERITIES = {
    SEVERITY.IGNORED: 'Ignored',
    SEVERITY.WARNING: 'Warning',
    SEVERITY.ERROR: 'Error',
}


class WorkerState(object):
    """This class holds the shared state of the different worker threads.
    """

    def __init__(self, *, use_unicode_conceal_as_level=SEVERITY.WARNING):
        # A lock to protect the state.
        self.lock = threading.Lock()
        # Blacklisted paths.
        self._blacklist = []
