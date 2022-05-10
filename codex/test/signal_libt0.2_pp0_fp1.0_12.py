import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from . import mainwindow

def main():
    app = QApplication(sys.argv)
    window = mainwindow.MainWindow()
    window.show()
    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(500)
