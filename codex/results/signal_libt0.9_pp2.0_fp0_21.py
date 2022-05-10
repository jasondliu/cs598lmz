import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PySide import QtGui, QtCore
from PySide.QtUiTools import QUiLoader
from PySide.QtCore import Qt
from PySide.QtGui import (QApplication, QTextEdit, QGridLayout, QPushButton,
                          QDialog, QHBoxLayout, QFont, QIcon, QFontDialog,
                          QVBoxLayout, QSizePolicy, QLabel)
import os

class Highlighter(QtGui.QSyntaxHighlighter):
    
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        self.colors = {
            'keyword': QtGui.QColor(92, 170, 255),
            'class': QtGui.QColor(0, 128, 128),
            'function': QtGui.QColor(100, 230, 230),
            'comment': QtGui.QColor(180, 180, 180),
            'string':
