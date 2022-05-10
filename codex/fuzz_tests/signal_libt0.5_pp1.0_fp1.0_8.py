import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtCore import QEvent, QObject, QThread, QTimer, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication

from . import settings
from . import log
from . import ui
from . import rpc
from . import wallet
from . import trade
from . import history
from . import address_dialog
from . import transaction_dialog
from . import password_dialog
from . import message_box
from . import util
from . import price_update


class Main(QObject):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.gui = None
        self.daemon = None
        self.wallet = None
        self.wallet_thread = None
        self.wallet_rpc = None
        self.wallet_rpc_thread = None
        self.trade = None
        self.trade_thread = None
        self.history
