import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtGui import QIcon

from .mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(":/icons/icons/app.png"))
    window = MainWindow()
    window.show()
    app.exec_()
