import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
import sys

from ui.mainwindow import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
