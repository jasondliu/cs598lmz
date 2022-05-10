from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("compressed.bz2", "rb").read())

# Using lz4 compression
import lz4
lz4.compress("this is a test")

# Using aes for encoding
import pyaes
key = 'this is a 16 byte key' # use a key from os.urandom(16) in real life
aes = pyaes.AESModeOfOperationCTR(key)
plain_text = 'test test test 1234'
cipher_text = aes.encrypt(plain_text)
decrypted_text = aes.decrypt(cipher_text)

# Using base64 encoding
import base64
base64.b64decode("c2VjcmV0")

# Using zlib compression
import zlib
s = 'witch which has which witches wrist watch'
print len(s)
t = zlib.compress(s)
print len(t)
print zlib.decompress(t)
print zlib.crc32(s)


# Using sha512 encryption
import hashlib

