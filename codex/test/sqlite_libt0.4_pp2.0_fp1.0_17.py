import ctypes
import ctypes.util
import threading
import sqlite3
import time
import random
import os
import sys
import json
import re
import math

from binascii import hexlify, unhexlify

from . import (config, util, exceptions, bitcoin, util)

from .i18n import _

# TODO: can this be removed?
# Used by format_satoshis() in history_list.py
# This constant is used to determine how many decimal places to display
# for certain currencies, e.g. BTC.  It's currently an int for
# performance reasons, as int-float multiplication is faster than int-Decimal.
DECIMAL_POINT_DEFAULT = 8

# TODO: can this be removed?
# Used by Transaction.get_amount()
_satoshis_str_to_int = lambda x: int(Decimal(x) * config.DECIMAL_POINT)
_satoshis_int_to_str = lambda x: str(Decimal(x) / config.DECIMAL_POINT)

# TODO: can this be removed?
# Used by Transaction.get
