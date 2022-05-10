import _struct
from Crypto.Util.number import *
from Crypto.Hash import SHA256


# for SHA1
block_size_sha1 = 64
iv_sha1 = 0x67452301
A_sha1 = 0x67452301
B_sha1 = 0xEFCDAB89
C_sha1 = 0x98BADCFE
D_sha1 = 0x10325476
E_sha1 = 0xC3D2E1F0


def add(x, y):
    return (x + y) & 0xFFFFFFFF

def sha1(msg):
    global A_sha1, B_sha1, C_sha1, D_sha1, E_sha1
    # if len(msg) > 0x2000000000000000: raise Exception("Too Long Message")
    _msg = padding_to_bits(msg)
    num = len(_msg) // 512
    for i in range(num):
        tmp = _msg[i*512:(i+1)*512]
        W = []
        for i in range(16):
           
