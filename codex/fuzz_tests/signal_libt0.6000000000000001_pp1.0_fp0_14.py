import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys

import qdarkstyle
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()


if __name__ == "__main__":
    main()
