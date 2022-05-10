import bz2
bz2.decompress(data)

#bz2.BZ2File('test.bz2')

import gzip
#gzip.open('test.gz')
#gzip.compress(data)

import zlib
#zlib.compress(data)

#zlib.crc32(data)

#import hashlib
#hashlib.md5(data).hexdigest()
#hashlib.sha1(data).hexdigest()
#hashlib.sha256(data).hexdigest()

import hmac
#hmac.new(key, message)

import random
#random.choice(string.ascii_letters)
#random.choice(string.ascii_letters + string.digits)
#random.randrange(10)
#random.randrange(0, 101, 2)

#random.shuffle(list)

#random.sample(xrange(100), 10)

#random.random()
#random.uniform(1, 10)
#random.normalvariate(0, 1)
