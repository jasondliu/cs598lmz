from bz2 import BZ2Decompressor
BZ2Decompressor_w = BZ2Decompressor()
def BZ2Decompress(data):
    return BZ2Decompressor_w.decompress(data)

def BZ2Compress(data):
    import io
    import bz2
    bio = io.BytesIO()
    bz2.compress(data, 1)

# bz2 is not faster than zlib, TODO use zlib
#def inflate(byte): return zlib.decompress(byte, 15) # 15: 1G buf, 20: unlimited
#def deflate(byte): return zlib.compress(byte, 1) # 1:huffman only, 9: best

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
CACHE = {}
def Ecryptor(key, iv):
    keyiv = key+iv
    if keyiv in CACHE:
        cryptor = CACHE.get(keyiv)
    else:
        cryptor = AES.new(key+iv, AES.MODE_CBC)
       
