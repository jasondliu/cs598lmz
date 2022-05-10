import _struct
from crc8 import CRC8

class EncodeError(Exception): pass
class DecodeError(Exception): pass

MAGIC = b'\xAA\x55'

HEADER_FORMAT = '>H'
HEADER_LEN	= struct.calcsize(HEADER_FORMAT)

class _Format(object):
	def __init__(self, fmt):
		self._fmt = _struct.Struct(fmt)
	
	def pack(self, *kwargs):
		return self._fmt.pack(*kwargs)

	def unpack(self, *kwargs):
		return self._fmt.unpack_from(*kwargs)

FMT_PUSH_REQUEST = '>BBBI'
FMT_PUSH_RESPONSE = '>BBB'
FMT_PULL_REQUEST = '>BBBQQQQQ'
FMT_PULL_RESPONSE = '>BBBI'
