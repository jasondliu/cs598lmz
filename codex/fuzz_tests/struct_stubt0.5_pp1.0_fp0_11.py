from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = Struct.calcsize(s.format)
print s.size

import os
print os.urandom(4)

import random
print random.randint(0, 2**32)

print random.getrandbits(32)

import time
print int(time.time())

import uuid
print uuid.uuid4().int

import hashlib
print hashlib.md5(str(uuid.uuid4())).hexdigest()

from Crypto import Random
print Random.get_random_bytes(4)

import base64
print base64.b64encode(os.urandom(6))

from binascii import hexlify
print hexlify(os.urandom(6))
