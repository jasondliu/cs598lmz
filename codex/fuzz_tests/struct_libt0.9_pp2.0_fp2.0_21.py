import _struct
import hashlib
import base58

import requests
import gevent
import gevent.pool
import gevent.monkey
gevent.monkey.patch_all(time=True, select=True, thread=False, os=True, ssl=True, httplib=True, aggressive=True)


MAX_ORPHAN_TRANSACTIONS = 1000000
MAX_CHAIN_LENGTH = 720

BLOCK_VERSION_GENESIS = 1
BLOCK_VERSION_DEPLOYMENT_TESTDUMMY = 2  # Also used by BLOCK_VERSION_DEPLOYMENT_ASSETS
BLOCK_VERSION_DEPLOYMENT_MERKLE_ROOT  = 3
BLOCK_VERSION_POW = 4


ADDRTYPE_P2PKH = 55
ADDRTYPE_P2SH = 85

WIF_TYPE_P2PKH = 128
WIF_TYPE_P2SH = 224

MIN_RELAY_TX_FEE = 100000
COINBASE_MATURITY = 100

TXFEE_ANON = (1.0
