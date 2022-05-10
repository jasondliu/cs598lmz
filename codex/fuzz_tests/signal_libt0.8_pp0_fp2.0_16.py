import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PySide import QtGui
import pyqtgraph as pg

from ratracks_gui.mainwindow import MainWindow


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
