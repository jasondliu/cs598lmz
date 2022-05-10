import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, QObject, pyqtSlot
from PyQt5.QtGui import QIcon

from src.gui.widgets.progress_bar import ProgressBar
from src.gui.widgets.log_widget import LogWidget
from src.gui.widgets.settings_widget import SettingsWidget
from src.gui.widgets.about_widget import AboutWidget
from src.gui.widgets.file_widget import FileWidget
from src.gui.widgets.file_list_widget import FileListWidget
from src.gui.widgets.file_list_item import FileListItem
from src.gui.widgets.file_list_item_widget import FileListItemWidget
from src.gui.widgets.file_list
