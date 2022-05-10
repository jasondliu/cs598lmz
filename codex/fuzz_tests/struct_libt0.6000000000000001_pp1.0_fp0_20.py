import _struct
from _struct import *
import pdb

def pack_byte(byte_val):
    return _struct.pack('B', byte_val)

def pack_char(char_val):
    return _struct.pack('c', char_val)

def pack_short(short_val):
    return _struct.pack('h', short_val)

def pack_ushort(ushort_val):
    return _struct.pack('H', ushort_val)

def pack_int(int_val):
    return _struct.pack('i', int_val)

def pack_uint(uint_val):
    return _struct.pack('I', uint_val)

def pack_long(long_val):
    return _struct.pack('l', long_val)

def pack_ulong(ulong_val):
    return _struct.pack('L', ulong_val)

def pack_longlong(longlong_val):
    return _struct.pack('q', longlong_val)

def pack_ulonglong(ul
