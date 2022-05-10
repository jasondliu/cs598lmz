import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PyQt")
        self.setGeometry(50, 50, 500, 300)

        extractAction = QtWidgets.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        openEditor = QtWidgets.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

