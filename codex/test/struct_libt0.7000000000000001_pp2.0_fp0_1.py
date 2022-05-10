import _struct

def _parse(s):
    for i in range(0, len(s), 4):
        yield _struct.unpack('>I', s[i:i+4])[0]

def _hash(s):
    a = 0x67452301
    b = 0xefcdab89
    c = 0x98badcfe
    d = 0x10325476
    for k in _parse(s):
        a = b + ((a + (k[0] + 0xd76aa478) + ((b & c) | (~b & d))) << 7 | (a + (k[0] + 0xd76aa478) + ((b & c) | (~b & d))) >> (32 - 7))
        d = a + ((d + (k[1] + 0xe8c7b756) + ((a & b) | (~a & c))) << 12 | (d + (k[1] + 0xe8c7b756) + ((a & b) | (~a & c))) >> (32 - 12))
