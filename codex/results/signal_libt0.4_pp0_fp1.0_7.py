import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.utils import resource_path

import sys
import os

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open(resource_path('style.qss'), "r").read())
    app.setWindowIcon(QIcon(resource_path('icon.png')))

    window = MainWindow()
    window.show()

    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)

    sys.exit(app.exec_())
