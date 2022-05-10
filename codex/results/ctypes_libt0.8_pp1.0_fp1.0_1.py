import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStackedLayout
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from src.ui.pages.home import Home
from src.ui.pages.settings import Settings
from src.ui.pages.study import Study

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.title = 'Flashcards'
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width,
