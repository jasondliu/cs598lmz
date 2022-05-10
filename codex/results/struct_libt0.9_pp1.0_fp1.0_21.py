import _struct

from binascii import hexlify, unhexlify
from hashlib import sha256
from struct import pack, unpack
from bitcoin.core import *
from bitcoin.core.serialize import Hash
from bitcoin.core.script import CScript, lshl, lshr, btc_to_satoshi
from bitcoin.core.key import CPubKey, CKey
from bitcoin.wallet import CBitcoinAddress
from bitcoin.rpc import Proxy

from bitcoinrpc.authproxy import JSONRPCException
from time import time, sleep
from copy import copy
import random
from decimal import Decimal
from itertools import chain
from operator import add
import sys


if (sys.version_info > (3, 0)):
    # In Python3 reduce() has moved to functools
    from functools import reduce

from . import util
from . import serialize


# genesis pubkey in hex
GENESIS_PUBKEY_HEX = '02f981e4c0708d293b38874998a7d2e87d21f9f21a
