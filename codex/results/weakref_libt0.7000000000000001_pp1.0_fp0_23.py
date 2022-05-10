import weakref
import functools
from typing import Optional

from PyQt5.QtCore import QObject, pyqtSignal as Signal
import numpy as np

import orangecanvas.utils as oc_utils
import orangecanvas.config as config

from orangecanvas.resources import icon_loader
from orangecanvas import config

from AnyQt.QtWidgets import (
    QApplication, QLabel, QMessageBox, QSizePolicy)

from .utils import gui
from .utils.gui import message_information
from .utils.async_ import (
    Async, async_, task_method, async_contextmanager, async_run)
from .utils.signals import (
    Output, Input, Single, Multiple, connect, disconnect)
from .utils.settingshandler import (
    ContextSetting, ListContextHandler,
    ContextSettingHandler)
from .utils.concurrent import Lock, FutureWatcher
from .utils.overlay import BusyOverlay
from .utils.overlay import OverlayWidget
from .utils.widgets import MessageOverlayWidget

from .
