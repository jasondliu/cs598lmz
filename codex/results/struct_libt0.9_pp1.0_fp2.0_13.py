import _struct as struct
from codecs import decode

from struct import pack as struct_pack
from struct import unpack as struct_unpack

from bitstring import BitArray
from bitstring import BitStream

from binascii import hexlify

from socket import SOCK_RAW, socket, IPPROTO_RAW

def dump(msg, cb=False, loc="0"):
    s = ''
    for i in range(0, len(msg)):
        if hex(int(msg[i])) == '0x0':
            if cb is True:
                if loc == '1':
                    if ord(msg[i]) == 0:
                        s += "\\x00"
                else:
                    s += ' '
            else:
                s += ' '
        else:
            s += "\\x%0.2x" % int(msg[i])
    return s


def u_to_ipaddr(addr):
    s = ''
    s += str(addr%256)
    while addr > 255:
        addr = addr >> 8
        s
