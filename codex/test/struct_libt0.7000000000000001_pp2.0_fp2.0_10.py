import _struct
import hashlib
import hmac

import requests

from ...core import (Bytes, BytesLike, ChecksumAddress, HexStr, HexStrBytes, TxParams, TxReceipt,
                     ValidationError, bytes_to_int, int_to_big_endian, to_checksum_address, to_hex, to_int)
from ...core.middleware import MiddlewareManager
from ...core.signing import create_transaction_signer, LocalAccount
from ...core.spoof import spoof_transaction_args
from ...core.tx_params import PredictionMarketParticipate
from ...formatting import is_address, is_binary_address, remove_0x_prefix, to_checksum_address, to_hex
from ...middleware import local_account_sign_middleware
