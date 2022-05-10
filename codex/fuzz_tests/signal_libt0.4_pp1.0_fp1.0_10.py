import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName('OpenMolar')
    app.setOrganizationDomain('openmolar.com')
    app.setApplicationName('OpenMolar')

    window = MainWindow()
    window.show()
    window.raise_()
    sys.exit(app.exec_())
