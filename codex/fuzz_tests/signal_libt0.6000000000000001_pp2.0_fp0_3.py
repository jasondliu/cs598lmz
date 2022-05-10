import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

import resources
# import api
# from api.core import qtapi
# from api import core
# from api import objects
# from api.qtapi import QtWidgets

from gui.mainwindow import MainWindow
from gui import utils

def main():
    # qtapi.debug.enable()
    # core.debug.enable()
    # objects.debug.enable()
    utils.debug.enable()

    app = QApplication(sys.argv)
    app.setStyleSheet(resources.style.DEFAULT)

    main_window = MainWindow()
    main_window.show()

    if len(sys.argv) > 1:
        main_window.add_tab(QUrl(sys.argv[1]))

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
