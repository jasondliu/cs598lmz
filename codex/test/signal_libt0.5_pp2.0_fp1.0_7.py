import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt

from twisted.internet.defer import inlineCallbacks

from client_tools.connection import connection
from client_tools.widgets import ClickableLabel

from client_tools.widgets.qt_generic_text_edit import QtGenericTextEdit


class SequenceEditor(QtWidgets.QWidget):
    def __init__(self, reactor, parent=None):
        super(SequenceEditor, self).__init__(parent)
        self.reactor = reactor
        self.make_layout()
        self.connect()
    
    def make_layout(self):
        self.sequence_label = ClickableLabel('Sequence:')
        self.sequence_label.clicked
