import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtGui, QtCore, QtWidgets

from gui.main_window import MainWindow
from gui.qt_utils import get_qicon

def main():
    app = QtWidgets.QApplication(sys.argv)

    app.setWindowIcon(get_qicon('icon.svg'))

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
