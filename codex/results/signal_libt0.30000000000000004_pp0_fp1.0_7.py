import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui

from . import mainwindow

def main():
    app = QtGui.QApplication(sys.argv)
    win = mainwindow.MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
