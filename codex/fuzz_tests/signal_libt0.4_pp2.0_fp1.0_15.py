import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication

from . import mainwindow

def main():
    app = QApplication(sys.argv)

    mw = mainwindow.MainWindow()
    mw.show()

    sys.exit(app.exec_())
