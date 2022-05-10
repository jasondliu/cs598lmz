import weakref

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QCheckBox, QComboBox, QSpinBox, QDoubleSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit, QListWidget, QListWidgetItem, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap

from . import utils
from . import settings
from . import data
from . import db
from . import widgets
from . import dialogs
from . import actions
from . import icons
from . import resources

class MainWindow(QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setWindowTitle("Pomodoro")
		self.setWindowIcon(QIcon(":/icons/pomodoro.png"))
		self.setMinimumSize(
