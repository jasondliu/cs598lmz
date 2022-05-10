import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys
import os
import os.path

from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

from lib.core import eskapade_config, eskapade_logger
from lib.core import eskapade_exceptions
from lib.core import eskapade_utils

from lib.gui import eskapade_icons

from lib.gui.widgets import eskapade_widgets

from lib.gui.pages.page_overview import PageOverview
from lib.gui.pages.page_details import PageDetails
from lib.gui.pages.page_editor import PageEditor
from lib.gui.pages.page_help import PageHelp


class EskaWindow(QtGui.QMainWindow):
    """Main Eskapade window."""

    _DEFAULT_GUI_STYLE = 'plastique'

    def __init__(self, parent=None):
        super(EskaWindow,
