import _struct
from binascii import hexlify
from socket import ntohs, ntohl

from scapy.automaton import Automaton, ATMT
from scapy.compat import orb, chb
from scapy.config import conf
from scapy.consts import WINDOWS, LINUX
from scapy.error import warning
from scapy.fields import (
    ByteEnumField, BitEnumField, BitField, BitFieldLenField, ByteField,
    FieldLenField, FlagsField, IntField, LELongField, LEIntField, LEShortField,
    MACField, PacketField, PacketListField, ShortEnumField, ShortField,
    StrField, StrFixedLenField, StrLenField, StrNullField, X3BytesField,
    XByteField, XShortField,
)
from scapy.layers.inet import IPerror, IP
from scapy.layers.inet6 import IPv6, _IPv6ExtHdr, _IPv6OptsHdr
from scapy.packet import (
    bind_layers,
