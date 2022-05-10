import weakref
import time
import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from electrum_ltc_gui.qt.util import *
from electrum_ltc_gui.qt.amountedit import AmountEdit
from electrum_ltc import Transaction
from electrum_ltc.util import print_error
from electrum_ltc.plugins import run_hook
from electrum_ltc.wallet import Multisig_Wallet

from electrum_ltc.i18n import _

class EnterButton(QPushButton):
    def __init__(self, text, func):
        QPushButton.__init__(self, text)
        self.func = func
        self.clicked.connect(func)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            apply(self.func,())

class MyTreeWidget(QTreeWidget):
    def __init__(self, parent):
        QTreeWidget.__init__(self, parent)

