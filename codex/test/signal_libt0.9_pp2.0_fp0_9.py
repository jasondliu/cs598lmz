import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import dbus

import QTermWidget

from qutepart import Qutepart
from pwiz import PWiz

from PyQt5.Qsci import QsciLexerPython, QsciScintilla
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import Q
