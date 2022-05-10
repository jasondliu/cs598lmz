import socket
socket.if_indextoname(1)

import struct
struct.unpack('&lt;L', struct.pack('&lt;L', 1))

from ctypes import Structure, windll, c_ulong
class MIB_IPFORWARDTABLE(Structure):
    _fields_ = [
        ('dwForwardDest', c_ulong),
        ('dwForwardMask', c_ulong),
        ('dwForwardPolicy', c_ulong),
        ('dwForwardNextHop', c_ulong),
        ('dwForwardIfIndex', c_ulong),
        ('dwForwardType', c_ulong),
        ('dwForwardProto', c_ulong),
        ('dwForwardAge', c_ulong),
        ('dwForwardNextHopAS', c_ulong),
        ('dwForwardMetric1', c_ulong),
        ('dwForwardMetric2', c_ulong),
        ('dwForwardMetric3', c_ulong),
        ('dwForwardMetric4', c_ulong),
        ('dwForwardMetric5',
