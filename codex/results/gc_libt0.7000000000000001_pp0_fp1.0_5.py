import gc, weakref
from struct import Struct, pack, unpack_from, calcsize
from binascii import hexlify, unhexlify
from datetime import datetime, timedelta
import re
from typing import (
    Tuple,
    Dict,
    Any,
    List,
    Optional,
    Sequence,
    Union,
    TYPE_CHECKING,
)

from .util import (
    dict_to_bytes,
    bytes_to_dict,
    PROTO_ID,
    hash_160,
    sha256,
    hmac_oneshot,
    bh2u,
    bfh,
    bh2u,
    Invoice,
    is_valid,
    bfh,
    bfh_hmac,
    int_to_hex,
    inv_dict,
    to_string,
    to_bytes,
    format_satoshis_plain,
    TxMinedInfo,
    assert_bytes,
    assert_str,
    assert_int,
    assert_type,
    assert
