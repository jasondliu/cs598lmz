import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import traceback
import argparse
import logging
import logging.handlers

from PyQt5.QtCore import QObject, pyqtSignal, QTimer
from PyQt5.QtWidgets import QApplication

from . import __version__
from . import config
from . import utils
from . import __appname__
from . import __description__
from . import __url__
from . import __author__
from . import __email__
from . import __license__
from . import __copyright__

from . import gui
from . import gui_utils
from . import gui_widgets
from . import gui_dialogs
from . import gui_signals
from . import gui_settings
from . import gui_config

from . import core
from . import core_config
from . import core_signals
from . import core_utils

from . import database
from . import database_config
from . import database_utils
from . import database_
