import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets

from vcc.utils import get_vcc_actions, init_vcc


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.app = app
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.resize(1024, 768)
        self.setWindowTitle("VCC2.0")
        self.setWindowIcon(QtWidgets.QIcon(":/icons/icons/favicon-32x32.png"))
        self.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.init_actions()
        self.init_menus()
        self.init_toolbars()
        self.init_statusbar()

        init_vcc(self)
        vcc_actions = get_v
