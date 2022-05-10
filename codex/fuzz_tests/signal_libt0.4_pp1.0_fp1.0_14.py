import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_help import Ui_Help

from ui_new_project import Ui_NewProject
from ui_settings import Ui_Settings
from ui_calibration import Ui_Calibration
from ui_calibration_dialog import Ui_CalibrationDialog
from ui_calibration_dialog_confirm import Ui_CalibrationDialogConfirm
from ui_calibration_dialog_info import Ui_CalibrationDialogInfo
from ui_calib
