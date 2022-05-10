import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_settings import Ui_Settings
from ui_preferences import Ui_Preferences
from ui_new_game import Ui_NewGame
from ui_game_over import Ui_GameOver
from ui_game_won import Ui_GameWon

from game import Game
from settings import Settings
from preferences import Preferences

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.settings = Settings()
        self.preferences = Preferences()

        self.game = Game
