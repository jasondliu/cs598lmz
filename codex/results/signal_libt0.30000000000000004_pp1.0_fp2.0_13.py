import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5.QtCore import QThread, pyqtSignal, QObject

from main_window import Ui_MainWindow
from data_loader import DataLoader
from data_processor import DataProcessor
from data_plotter import DataPlotter
from data_saver import DataSaver
from data_reader import DataReader

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Программа для обработки данных о скорости ветра")

        self.data_loader = DataLoader()
        self.data_processor =
