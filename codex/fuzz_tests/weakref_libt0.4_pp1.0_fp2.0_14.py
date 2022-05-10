import weakref
import time

from PySide.QtCore import *
from PySide.QtGui import *

from . import utils
from . import settings
from . import model
from . import view
from . import controller
from . import resources

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('PyLint GUI')
        self.setWindowIcon(QIcon(':/icons/pylint.png'))
        self.resize(QSize(800, 600))
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()
        self.model = model.Model()
        self.view = view.View(self.model)
        self.controller = controller.Controller(self.model, self.view)
        self.controller.set_status_bar(self.statusBar())
        self.controller.set_main_window(self)
        self.set
