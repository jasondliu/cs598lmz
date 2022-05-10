import weakref
from logging import getLogger
from twisted.internet import defer
from twisted.internet.defer import fail, succeed
from twisted.python.failure import Failure
from zope.interface import implements
from zope.interface.exceptions import DoesNotImplement
from zope.interface.verify import verifyObject

from . import (
    interfaces,
)
from .exc import (
    InvalidTransactionID,
    NotEnoughFunds,
    NotEnoughTokens,
    NoPathError,
)
from .util import (
    NotEnoughFundsError,
)

log = getLogger(__name__)


class BaseExchange(object):
    """
    A base class for implementing exchanges.

    Exchanges are used to swap between two tokens in a single transaction.
    """
    def __init__(self):
        self.locked = False
        self.lock_transaction = None
        self.lock_deferred = None

