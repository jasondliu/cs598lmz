import gc, weakref

from . import util
from . import ui

class Dialog(ui.Dialog):
    def __init__(self, size, title, parent=None):
        ui.Dialog.__init__(self, parent)
        self.title = title
        self.size = size
        self.setWindowTitle(self.title)
        self.setFixedSize(*size)
        self.center()

        self.setObjectName("Dialog")
        self.setStyleSheet("""
        QDialog {
            background-color: #1D1F21;
            color: #C5C8C6;
            border: 1px solid #282A2E;
        }
        QPushButton {
            background-color: #373B41;
            color: #C5C8C6;
            border: 1px solid #282A2E;
        }
        QPushButton:hover {
            background-color: #3B4549;
            color: #C5C8C6;
        }
        QPushButton:pressed {
            background-color
