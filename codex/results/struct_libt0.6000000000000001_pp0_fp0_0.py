import _struct

# python 2/3 compatibility
try:
    range = xrange
except NameError:
    pass

__all__ = ['Packet', 'PacketStream', 'PacketHeader', 'PacketFactory',
           'PacketError', 'ErrorPacket', 'PacketType', 'PacketParser',
           'PacketParserError', 'PacketParserEOF']

# constants
MAX_PACKET_SIZE = 32768
MIN_PACKET_SIZE = 8
MAX_PACKET_SIZE_BYTES = 4
MIN_PACKET_SIZE_BYTES = 1
PACKET_HEADER_SIZE = 8
PACKET_HEADER_SIZE_BYTES = 2

# packet types
PACKET_TYPE_ERROR = 0
PACKET_TYPE_DATA = 1
PACKET_TYPE_ACK = 2
PACKET_TYPE_HELLO = 3
PACKET_TYPE_BYE = 4

# error codes
ERROR_CODE_INVALID_PACKET = 0
ERROR_CODE_MALFORMED_P
