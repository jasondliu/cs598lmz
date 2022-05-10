import ctypes
ctypes.windll.user32.SetProcessDPIAware()

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

from src import constants
from src.common import (get_screen_size, get_working_area,
                        get_icons_path, get_settings_path,
                        is_window_overlapping_with_any_other)
from src.window import Window
from src.buttons import SettingsButton, ExitButton, MinimiseButton
from src.settings_dialog import SettingsDialog


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setObjectName("main
