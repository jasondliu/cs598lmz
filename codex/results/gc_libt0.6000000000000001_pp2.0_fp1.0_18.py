import gc, weakref
import re

from twisted.internet import defer
from twisted.internet import reactor
from twisted.python import log

from ..helpers import deferToDatabase, deferToThread
from ..helpers import get_uuid
from ..helpers import json_dumps, json_loads
from ..helpers import NotEnoughFunds, WrongPassword, InvalidPassword, InvalidSecret
from ..helpers import InvalidDestinationAddress, InvalidBitcoinAddress, InvalidBip38Key

from .exchange_rate_manager import ExchangeRateManager

class BlockchainInfoProvider(object):

    _instance = None
    _instances = weakref.WeakValueDictionary()

    def __new__(cls, *p, **k):
        if BlockchainInfoProvider._instance is None:
            BlockchainInfoProvider._instance = object.__new__(cls)
        return BlockchainInfoProvider._instance

    def __init__(self, config=None):
        if config is None: config = {}

        self.network = None

        if config.get('BLOCKCHAIN_SERVICE_NAME') == 'blockchain.info':
            # only
