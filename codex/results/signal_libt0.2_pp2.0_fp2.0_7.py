import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

from mainwindow import MainWindow
from config import Config
from config import ConfigError

import sys

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Qt5-Webcam")
    app.setOrganizationName("Qt5-Webcam")
    app.setOrganizationDomain("qt5-webcam.org")
    app.setApplicationVersion("0.1")

    try:
        config = Config()
    except ConfigError as e:
        print("Error: {}".format(e))
        sys.exit(1)

    window = MainWindow(config)
    window.show()

    timer = QTimer()
    timer.timeout.connect(window.update_frame)
    timer.start(1000.0 / config.fps)

    sys.exit(app.exec_())

if __
