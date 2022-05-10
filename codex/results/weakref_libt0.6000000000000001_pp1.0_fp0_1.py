import weakref

from PyQt5.QtGui import QColor, QFont, QTextCharFormat
from PyQt5.QtWidgets import QTextEdit, QWidget, QStyleOption, QStyle, QApplication
from PyQt5.QtCore import Qt, QSize, QRect, QTimer, QPoint, QObject, QEvent, pyqtSignal

from .utils import format_line, format_token
from .editor import TextEditor
from .highlighter import Highlighter
from .syntax import Syntax
from .styles import Styles
from .linenumbers import LineNumbers
from .tooltip import Tooltip
from .completer import Completer
from .settings import Settings
from .settingswindow import SettingsWindow
from .api import API
from .theme import Theme
from . import styles
from . import completer
from . import syntax
from . import api
from . import theme


class Core(QObject):
    
    # Signals
    text_changed = pyqtSignal()
    cursor_position_changed = pyqtSignal()
    update_request =
