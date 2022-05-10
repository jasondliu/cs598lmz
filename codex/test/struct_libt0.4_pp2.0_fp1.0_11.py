import _struct

def _pack_int(i):
    if i < 0x80:
        return chr(i)
    elif i < 0x4000:
        return chr((i >> 8) | 0x80) + chr(i & 0xff)
    elif i < 0x200000:
        return chr((i >> 16) | 0xc0) + chr((i >> 8) & 0xff) + chr(i & 0xff)
    elif i < 0x10000000:
        return chr((i >> 24) | 0xe0) + chr((i >> 16) & 0xff) + chr((i >> 8) & 0xff) + chr(i & 0xff)
    else:
        return chr(0xf0) + chr((i >> 24) & 0xff) + chr((i >> 16) & 0xff) + chr((i >> 8) & 0xff) + chr(i & 0xff)

def _unpack_int(s):
    c = ord(s[0])
