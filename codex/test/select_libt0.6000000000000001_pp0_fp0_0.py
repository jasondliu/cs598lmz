import select
import sys
import threading
import time
import traceback
from collections import deque
from datetime import datetime
from decimal import Decimal
from io import BytesIO
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union

import bitcoin
import ecdsa
import requests
import requests.exceptions
from bitcoin import SelectParams
from bitcoin.core import CTransaction, CMutableTransaction
from bitcoin.core.script import CScript, OP_CHECKSIG
from bitcoin.core.scripteval import VerifyScript, SCRIPT_VERIFY_P2SH
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from bitcoin.wallet import P2SHBitcoinAddress
from ecdsa import VerifyingKey
from requests.exceptions import ConnectionError, Timeout

from electrumsv.constants import COIN, DUST_THRESHOLD, MAX_FEE_RATE, MIN_RELAY_TX_FEE
from electrumsv.crypto import ec_key_from_text
