import _struct

def unpack_from(format, buffer, offset=0):
  return _struct.unpack_from(format, buffer, offset)

def pack_into(format, buffer, offset, *args):
  return _struct.pack_into(format, buffer, offset, *args)

def calcsize(format):
  return _struct.calcsize(format)

Ethernet = namedtuple('Ethernet', 'dst src ethertype data')
IP = namedtuple('IP', 'version ihl tos len id flags frag_off ttl proto src dst data')
ICMP = namedtuple('ICMP', 'type code checksum data')

def parse_ethernet(data):
  return Ethernet(*unpack_from('!6s6sH', data))

def parse_ip(data):
  version_ihl = unpack_from('!B', data)[0]
  version = version_ihl >> 4
  ihl = version_ihl & 0xF
  return IP(version, ihl, *unpack_from('!
