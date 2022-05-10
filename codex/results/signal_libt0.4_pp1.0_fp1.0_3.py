import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QSettings

import sys

import app.main

def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("QtProject")
    app.setOrganizationDomain("qt-project.org")
    app.setApplicationName("Qt Creator")
    app.setApplicationVersion("4.0.0")
    app.setStyleSheet(open('./app/style.css').read())
    app.setWindowIcon(QIcon("./app/icon.png"))
    app.main = app.main.Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
