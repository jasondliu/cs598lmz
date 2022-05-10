import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import inspect

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt

from .gui.main_window import Ui_MainWindow
from .gui.about_dialog import Ui_AboutDialog
from .gui.settings_dialog import Ui_SettingsDialog
from .gui.preferences_dialog import Ui_PreferencesDialog
from .gui.preferences_page_general import Ui_PreferencesPageGeneral
from .gui.preferences_page_editor import Ui_PreferencesPageEditor
from .gui.preferences_page_terminal import Ui_PreferencesPageTerminal
from .gui.preferences_page_filetypes import Ui_PreferencesPageFiletypes
from .gui.preferences_page_themes import Ui_PreferencesPageThemes
from .gui.preferences_page_shortcuts import Ui_PreferencesPageShortcuts
from .gui.preferences_
