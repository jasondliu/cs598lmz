import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4.QtGui import QApplication, QMainWindow
from PyQt4.QtCore import QObject, SIGNAL, pyqtSlot

from ui.ui_mainwindow import Ui_MainWindow
from ui.dialogs.newPlayerDialog import NewPlayerDialog
from ui.dialogs.newGameDialog import NewGameDialog
from ui.dialogs.configureDialog import ConfigureDialog
from ui.frames.gameWidget import GameWidget
from ui.frames.playerWidget import PlayerWidget

from game import Game
from player import Player

# TODO:
#   - implement Hint
#   - implement Undo
#   - implement Load Game

class MainWindow(QMainWindow):
    """
    The main window for the application.
    """
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(
