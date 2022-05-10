import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

from main_window import MainWindow
from config import Config
from serial_manager import SerialManager
from mavlink_manager import MavlinkManager
from logger import Logger
from file_manager import FileManager
from plot_manager import PlotManager
from mission_manager import MissionManager
from telemetry_manager import TelemetryManager


class MainThread(QThread):
    """
    Main thread that runs the whole application.
    """

    def __init__(self, config_file):
        super(MainThread, self).__init__()

        self.config = Config(config_file)
        self.logger = Logger(self.config.get_log_level())
        self.serial = SerialManager(self.config, self.logger)
        self.mavlink = MavlinkManager(self.config, self.
