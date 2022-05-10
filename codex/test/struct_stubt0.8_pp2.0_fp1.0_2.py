from _struct import Struct
s = Struct.__new__(Struct)
s.format = '=B'
s.size = struct.calcsize(s.format)
s.unpack_from = m_unpack_from = s.unpack_from

def m_unpack(buf):
  return m_unpack_from(buf, 0)

s.unpack = m_unpack

def vscp_msg_decode(buf):
  offset = 0
  msg = {}

  msg['crc'], = s.unpack_from(buf, offset)
  offset += s.size

  if msg['crc'] != 0xE5:
    msg['head'], = struct.unpack_from('=B', buf, offset)
    offset += struct.calcsize('=B')

    msg['priority'], = struct.unpack_from('=B', buf, offset)
    offset += struct.calcsize('=B')

    msg['class'], = struct.unpack_from('=H', buf, offset)
    offset += struct.calcsize('=H')

