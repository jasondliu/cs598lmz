import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n' * 100)).start()

import logging
logging.basicConfig(filename='debug.log',level=logging.DEBUG)

from PySide import QtCore, QtGui
from PySide.QtCore import Qt
from PySide.QtGui import QApplication

from gui.mainwindow import MainWindow

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = MainWindow()
    app.setActiveWindow(win)
    sys.exit(app.exec_())
