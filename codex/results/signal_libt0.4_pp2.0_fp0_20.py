import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from gui.qt.main_window import MainWindow
from gui.qt.qt_thread import QtThread
from gui.qt.qt_thread import QtThread

from gui.qt.qt_thread import QtThread
from gui.qt.qt_thread import QtThread

from gui.qt.qt_thread import QtThread


class GuiController(QObject):
    """
    Controller of the GUI.
    """

    # Signals
    signal_start_qt_thread = pyqtSignal()
    signal_stop_qt_thread = pyqtSignal()
    signal_start_main_window = pyqtSignal()

    def __init__(self, parent=None):
        super(GuiController, self).__init__(parent)
        self.app = QApplication(sys.argv)
        self.thread = Qt
