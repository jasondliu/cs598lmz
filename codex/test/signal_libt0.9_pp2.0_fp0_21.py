import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PySide import QtGui, QtCore
from PySide.QtUiTools import QUiLoader
from PySide.QtCore import Qt
from PySide.QtGui import (QApplication, QTextEdit, QGridLayout, QPushButton,
                          QDialog, QHBoxLayout, QFont, QIcon, QFontDialog,
                          QVBoxLayout, QSizePolicy, QLabel)
import os
