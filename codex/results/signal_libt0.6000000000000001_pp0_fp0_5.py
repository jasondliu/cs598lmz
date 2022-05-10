import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui

from mainwindow import MainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
