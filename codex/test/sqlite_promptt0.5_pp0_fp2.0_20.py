import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

#from ctypes import *

import os
import sys
import time
import traceback

from PyQt4 import QtCore, QtGui, QtSql
from PyQt4.QtCore import Qt

from ui.ui_mainwindow import Ui_MainWindow
from ui.ui_about import Ui_AboutDialog
from ui.ui_config import Ui_ConfigDialog
from ui.ui_config_general import Ui_ConfigGeneral
from ui.ui_config_plugins import Ui_ConfigPlugins
from ui.ui_config_plugins_edit import Ui_PluginDialog
from ui.ui_config_plugins_edit_arguments import Ui_PluginArgumentsDialog
from ui.ui_config_plugins_edit_arguments_list import Ui_PluginArgumentsListDialog
from ui.ui_config_plugins_edit_arguments_list_item import Ui_PluginArgumentsListItemDialog
from ui.ui_config_plugins_edit_arguments_list_item_add import Ui_
