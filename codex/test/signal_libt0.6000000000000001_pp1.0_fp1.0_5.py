import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui, QtCore

from omelette.fromage.common import log
from omelette.fromage.ui.common import UiLoader
from omelette.fromage.ui.authentication import AuthenticationDialog
from omelette.fromage.ui.about import AboutDialog
from omelette.fromage.ui.lobby import Lobby
from omelette.fromage.ui.game import Game
from omelette.fromage.ui.host import HostDialog

from omelette.compiler.parser import Parser

class Application(QtGui.QApplication):
    def __init__(self, parser):
        QtGui.QApplication.__init__(self, [])
        self.connect(self, QtCore.SIGNAL("lastWindowClosed()"), self.quit)
        self.parser = parser
        self.ui_loader = UiLoader(self)
        self.authentication = AuthenticationDialog(self)
        self.lobby
