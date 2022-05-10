import _struct
import struct

def ntohs(int):
    return struct.unpack("!H", struct.pack("H",int))[0]

def ntohl(int):
    return struct.unpack("!I", struct.pack("I",int))[0]

def htonl(int):
    return struct.unpack("!I", struct.pack("I",int))[0]

def htons(int):
    return struct.unpack("!H", struct.pack("H",int))[0]
