import _struct
from PyQt5 import QtCore, QtWidgets, uic
from gui import Ui_MainWindow
from app_state import AppState
from load_file import load_file
from save_file import save_file
from render_options import render_options
from render_channels import render_channels
from render_struct import render_struct
from render_editor import render_editor


class Controller:

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.app_state = AppState()
        self.ui.tree_files.currentItemChanged.connect(self.tree_files_selection_changed)
        self.ui.tree_files.itemChanged.connect(self.tree_files_item_changed)
