import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QObject, pyqtSignal

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QCheckBox

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (QWidget, QToolTip, 
    QPushButton, QApplication, QMessageBox, QDesktopWidget)

from PyQt5.QtGui import QFont    


class MyWin(QWidget):
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle("Тестовое окно")
        self.resize(300, 200)
        self
