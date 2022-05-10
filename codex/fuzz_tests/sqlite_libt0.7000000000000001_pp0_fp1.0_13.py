import ctypes
import ctypes.util
import threading
import sqlite3

from PyQt4.QtGui import QAction, QMenu, QIcon, QKeySequence
from PyQt4.QtCore import QObject, SIGNAL
from PyQt4.Qt import qDebug, QApplication

from ninja_ide import resources
from ninja_ide.core import plugin
from ninja_ide.core import file_manager
from ninja_ide.tools import ui_tools
from ninja_ide.tools.completion import completer_widget
from ninja_ide.gui.main_panel import main_container
from ninja_ide.gui.editor import checker
from ninja_ide.gui.editor import highlighter
from ninja_ide.gui.editor import nedit
from ninja_ide.gui.editor import completion_thread
from ninja_ide.gui.editor import completion_hinter
from ninja_ide.gui.editor import type_hinter
from ninja_ide.gui.editor import code_completion
from ninja_ide.gui.editor import line_number_widget
from ninja_ide.gui.editor import folding_widget
from ninja_ide.gui.
