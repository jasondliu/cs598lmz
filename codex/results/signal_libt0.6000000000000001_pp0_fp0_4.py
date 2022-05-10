import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from datetime import datetime
from time import sleep
from os import path, mkdir
from threading import Thread, enumerate as thr_enumerate
from shutil import rmtree
import sys

from ui.main_window import Ui_MainWindow
from ui.new_game_dialog import Ui_NewGameDialog
from ui.game_over_dialog import Ui_GameOverDialog
from ui.game_settings_dialog import Ui_GameSettingsDialog
from ui.player_settings_dialog import Ui_PlayerSettingsDialog
from ui.preferences_dialog import Ui_PreferencesDialog
from ui.game_report_dialog import Ui_GameReportDialog
from ui.save_game_dialog import Ui_SaveGameDialog
from ui.load_game_dialog
