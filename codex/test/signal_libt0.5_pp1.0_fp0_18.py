import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

from gui import Ui_Form

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.button_open.clicked.connect(self.open_file)
        self.ui.button_save.clicked.connect(self.save_file)
        self.ui.button_add.clicked.connect(self.add_item)
        self.ui.button_delete.clicked.connect(self.delete_item)
        self.ui.button_edit.clicked.connect(self.edit_item)

