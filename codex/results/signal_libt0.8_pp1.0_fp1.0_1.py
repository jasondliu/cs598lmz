import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import com.common as common
from com.base_class.qt_class import MainWindow

from gui.qss.qss import *
from gui.qss.qss import *


def main():
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("惠州妇女病科")
    app.setStyleSheet(MAIN_QSS)
    app.setStyle("Fusion")

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
