import weakref

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QCheckBox

from . import config
from . import utils
from . import log
from . import settings

class SettingsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        self.settings = settings.Settings()

        self.layout().addWidget(self.createLoggingSettings())
        self.layout().addWidget(self.createConnectionSettings())
        self.layout().addWidget(self.createMiscSettings())

        self.layout().addStretch(1)

        self.show()

    def createLoggingSettings(self):
