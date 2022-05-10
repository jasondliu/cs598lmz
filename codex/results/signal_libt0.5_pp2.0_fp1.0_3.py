import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_AboutWindow
from ui_options import Ui_OptionsWindow
from ui_save import Ui_SaveWindow
from ui_load import Ui_LoadWindow

from gui_helpers import *
from gui_options import *
from gui_load import *
from gui_save import *
from gui_about import *
from gui_editor import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle("Kirby's Dream Land 3 Level Editor")

        self.setWindowIcon(
