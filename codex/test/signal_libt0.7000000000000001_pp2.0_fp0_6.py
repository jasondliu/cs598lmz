import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QDesktopWidget, QWidget, QLineEdit, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
from PyQt5.QtCore import Qt

from pyfridge import PyFridge

class PyFridgeGui(QWidget):
    def __init__(self, pyfridge):
        super().__init__()
        self.pyfridge = pyfridge
        self.initUI()

    def initUI(self):      
        self.resize(400, 200)
        self.setWindowTitle('PyFridge')
        self.moveToCenter()

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#525252'))
        self.setPalette(p)

        self.line = QLineEdit(self)
