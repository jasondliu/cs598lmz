import gc, weakref
import sys
import time
import traceback
from collections import defaultdict
from functools import partial
from inspect import signature
from threading import Thread
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from PyQt5.QtCore import QObject, QThread, QTimer, pyqtSignal

from electrumsv.constants import SVMainnet
from electrumsv.exceptions import InvalidPassword, UserCancelled
from electrumsv.i18n import _
from electrumsv.logs import logs
from electrumsv.networks import Network
from electrumsv.util import bfh, bh2u, to_string

from . import util
from .util import (InvalidPasswordException, MessageBoxException,
    NetworkException, UserCancelledException)

if False:
    from . import ElectrumWindow
    from .main_window import ElectrumGui

logger = logs.get_logger("daemon")

class DaemonThread(QThread):
    daemon_updated = pyqtSignal()

    def __
