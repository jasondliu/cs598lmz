from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'ps'
s.size = Struct.calcsize(s.format)
def unpack(buf, i=0):
  return (Struct.unpack_from(s.format, buf, i), i+s.size)

# -------------------
# PUNNET_KEY_REQ_HDR
# -------------------

from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'b'
s.size = Struct.calcsize(s.format)
def unpack(buf, i=0):
  return (Struct.unpack_from(s.format, buf, i), i+s.size)

# ------------------------
# PUNNET_KEY_REQ_HDR_BITS
# ------------------------

class KEY_REQ_HDR_BITS_dev_info(object):
  __slots__ = ['slave_id', 'prog_key_id', 'hard_key_id']

  def __init__(self, slave_id=0, prog_key_id=0, hard_
