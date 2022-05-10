import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

import sys

import ui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("PyQt5")
    window = ui.MainWindow()
    window.show()
    sys.exit(app.exec_())
