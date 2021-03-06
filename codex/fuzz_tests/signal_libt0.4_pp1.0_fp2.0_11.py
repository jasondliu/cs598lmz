import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui

from mainwindow import MainWindow

def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
