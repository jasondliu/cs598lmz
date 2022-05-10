import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(str(u"kabaret.gui"))

import logging
from kabaret.gui.app.app import App
from kabaret.gui.app.config import Config
from kabaret.gui.app.session import Session

from . import core
from . import client_tracker
from . import settings
from . import concurrency
from .debug import debug
from .server import Server
from .protocol import Protocol
from . import actions
from . import errors

from .client_tracker import sys_clients, this_client
from . import commands as cli_commands

from .text import TR
from .core.exceptions import NotHandledScriptError, NotSupportedScriptError

from PySide import QtGui, QtCore
from PySide.QtCore import Signal, Slot

from .log import msg_logger

from .core import concurrency

logger = logging.getLogger('kabaret.gui.cliconsole')

class ClientApp(App):
    def init(self):

