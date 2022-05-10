import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import logging
logging.basicConfig(level=logging.DEBUG)

import sys
import os
import time
import threading
import Queue
import traceback
import ConfigParser

from PyQt4 import QtGui, QtCore, QtWebKit

from lib.core import *
from lib.utils import *
from lib.db_utils import *
from lib.plugins import *

from ui.main_window import Ui_MainWindow
from ui.about_dialog import Ui_AboutDialog
from ui.settings_dialog import Ui_SettingsDialog
from ui.add_plugin_dialog import Ui_AddPluginDialog
from ui.add_plugin_dialog import Ui_AddPluginDialog
from ui.add_plugin_dialog import Ui_AddPluginDialog

from ui.plugin_settings_dialog import Ui_PluginSettingsDialog

from ui.plugin_settings_dialog import Ui_PluginSettingsDialog
