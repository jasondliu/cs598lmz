import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer

from ui_mainwindow import Ui_MainWindow
from ui_about import Ui_About
from ui_settings import Ui_Settings
from ui_progress import Ui_Progress
from ui_progress_thread import Ui_ProgressThread
from ui_progress_thread_single import Ui_ProgressThreadSingle
from ui_progress_thread_multi import Ui_ProgressThreadMulti
from ui_progress_thread_multi_single import Ui_ProgressThreadMultiSingle
from ui_progress_thread_multi_single_sub import Ui_ProgressThreadMultiSingleSub
from ui_progress_thread_multi_single_sub_sub
