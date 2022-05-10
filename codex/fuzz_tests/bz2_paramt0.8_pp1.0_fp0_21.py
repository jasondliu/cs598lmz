from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(s)

s = b'some bytes'
s = s.replace(b'bytes', b'bits')

s = b'some bytes'
for c in s:
    print(c)

# Convert bytes to string
s = b'Hello World'
s.decode('ascii')

s = 'Hello World'
s.encode('utf-8')

s = b'Hello World'
s.decode('ascii'), s.decode('utf-8')

s = 'Hello World'
s.encode('ascii'), s.encode('utf-8')

# Byte patterns
import re
pat = re.compile('b[a-f]')

b = pat.match(b'ba')
b.group()

b = pat.match(b'ba', pos=1)

b = pat.match(b'bb', pos=1)
b.group()

b = pat.match(b'fa', pos=1)
b.group()

# Example: Reading and Writing
