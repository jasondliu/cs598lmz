import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
from PyQt4 import QtGui
import os.path

# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "src"))

import test_unit
test_unit.init()

from ui.main_window import MainWindow

def main():
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Mangareader")

    window = MainWindow()
    # window.showMaximized()
    window.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
