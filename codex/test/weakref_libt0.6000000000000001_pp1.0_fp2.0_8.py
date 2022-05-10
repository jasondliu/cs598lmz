import weakref

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QGridLayout, QLabel, QSizePolicy, QWidget

from .colors import ColorScheme
from .qt_utils import get_monospace_font
from .widgets.button import Button
from .windows.main_window import MainWindow


class InfoBar(QWidget):
    """A widget for displaying information about a test."""

    def __init__(self, parent: QWidget = None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.setMinimumWidth(300)
        self.setMaximumHeight(100)
        self._test_name = None
        self._test_status = None
        self._test_message = None
        self._test_message_options = {}
        self._test_icon = None
        self._test_
