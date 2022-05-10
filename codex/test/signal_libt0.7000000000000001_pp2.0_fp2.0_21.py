import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QInputDialog
from PyQt5.QtGui import QPixmap, QImage
from pathlib import Path
from natsort import natsorted

from UI_Files.ui_mainwindow import Ui_MainWindow
from modules.ui.UI_Main import UI_Main
from modules.ui.UI_Settings import UI_Settings
from modules.ui.UI_Data import UI_Data
from modules.ui.UI_Video import UI_Video
from modules.ui.UI_Image import UI_Image
from modules.ui.UI_Logs import UI_Logs
from modules.ui.UI_Help import UI_Help
from modules.ui.UI_About import UI_About

