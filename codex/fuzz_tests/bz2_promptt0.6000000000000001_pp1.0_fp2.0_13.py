import bz2
# Test BZ2Decompressor class
decomp = bz2.BZ2Decompressor()
decomp.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
decomp.flush()

import bz2
# Test BZ2File class
f = bz2.BZ2File('sample.bz2', 'rb')
f.read()
f.close()

import bz2
# Test BZ2File class with context manager
with bz2.BZ2File('sample.bz2', 'rb') as f:
    f.read()

import calendar
# Test Calendar module
calendar.isleap(2000)

import calendar
# Test Calendar module
calendar.isleap(1900)

import calendar
# Test Calendar module
calendar.isleap(2004)
