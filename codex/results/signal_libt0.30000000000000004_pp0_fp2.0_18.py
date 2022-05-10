import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5 import QtCore, QtWidgets

from . import __version__
from . import __description__
from . import __author__
from . import __email__
from . import __url__

from . import __appname__

from . import __copyright__

from . import __license__


class AboutDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)

        self.setWindowTitle("About")

        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        self.setMinimumSize(QtCore.QSize(400, 300))

        self.setMaximumSize(QtCore.QSize(400, 300))

        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.setMod
