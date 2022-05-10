import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer

from . import mainwindow

app = QtWidgets.QApplication(sys.argv)

def main():
    window = mainwindow.MainWindow()
    window.show()

    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(100)

    sys.exit(app.exec_())
