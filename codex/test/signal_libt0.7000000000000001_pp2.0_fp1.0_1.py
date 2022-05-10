import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
if sys.version_info >= (3, 0):
    from urllib.request import urlopen
    from urllib.error import URLError
else:
    from urllib2 import urlopen
    from urllib2 import URLError

from PySide.QtCore import *
from PySide.QtGui import *

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setMinimumSize(600, 400)

        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.text.setFontFamily('Courier')
        self.text.setFontPointSize(12)
        self.text.setAcceptDrops(True)
        self.text.setLineWrapMode(QTextEdit.NoWrap)
