import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog
from PyQt5.QtCore import QCoreApplication, QSettings, QTranslator, qVersion
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QEvent
from PyQt5.QtCore import Qt

from .gui.main_window import Ui_MainWindow
from .gui.about_dialog import AboutDialog
from .gui.new_project_dialog import NewProjectDialog
from .gui.new_file_dialog import NewFileDialog
from .gui.new_folder_dialog import NewFolderDialog
from .gui.project_properties_dialog import ProjectPropertiesDialog
from .gui.file_properties_dialog import FilePropertiesDialog
from .gui.rename_file_dialog import RenameFileDialog
from .gui.rename
