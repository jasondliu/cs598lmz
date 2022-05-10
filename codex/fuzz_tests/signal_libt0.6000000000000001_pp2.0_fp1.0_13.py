import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from gui.widgets.infopanel import InfoPanel
from gui.widgets.filepanel import FilePanel
from gui.widgets.menubar import MenuBar
from gui.widgets.toolbar import ToolBar
from gui.widgets.statusbar import StatusBar

from gui.dialogs.aboutdialog import AboutDialog
from gui.dialogs.settingsdialog import SettingsDialog

from gui.widgets.datapanel import DataPanel
from gui.widgets.plotpanel import PlotPanel

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # create application object
        self.app = QApplication.instance()

        # init main window
        self.initUI()

        # init data
        self.initData
