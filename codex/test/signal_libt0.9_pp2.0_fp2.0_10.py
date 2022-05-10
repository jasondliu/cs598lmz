import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from qcombination.mainwindow import MainWindow

if __name__ == "__main__":
    qcombination.VERSION = "0.9.6"
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
