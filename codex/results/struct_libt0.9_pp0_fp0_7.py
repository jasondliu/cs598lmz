import _struct
from collections import OrderedDict, Sequence
from logging import getLogger
from sys import argv, stdout
from typing import Dict, Generator, Iterable, Iterator, List, Optional, Tuple, Type, Union, cast

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey, ed25519

from common.convert import HexColor, HexColors, hex_color
from common.exceptions import ProtocolError, TransientError
from common.iterable import iterable_chunked
from common.keys import PublicKey
from common.serialization import (
    BinarySerializable,
    BootstrapNodeDescriptor,
    Deserializer,
    DeserializerError,
    deserialize_list,
    serialize_list,
    serialize_naked_message_type,
    serialize_raw,
    serialize_signed,
)
from . import (
    Address,
    CalledProcessError,
    Port,
    check_connection,

