import _struct
from binascii import hexlify, unhexlify
from itertools import groupby
from collections import defaultdict
from pprint import pprint
from time import time

from . import (util, config, bitcoin, exceptions, util)
from . import (Order, Trade)
from .util import bfh, bh2u, UserCancelled
from .bitcoin import double_sha256, hash_encode, hash_decode, public_key_to_p2pkh
from .transaction import Transaction
from .bip32 import BIP32Node
from .logging import get_logger


_logger = get_logger(__name__)


class TradesViewItem(util.PrintError):
    pass


class TradesModel(QtCore.QObject):
    content_updated = pyqtSignal()
    header_updated = pyqtSignal()

    def __init__(self, parent, window, order_book_id, my_addresses, fiat_unit):
        super().__init__(parent)
        self.window = window

