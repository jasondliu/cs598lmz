import bz2
# Test BZ2Decompressor.read()

try:
    bz2.BZ2Decompressor
except AttributeError:
    print("lskdjf")
    raise SystemExit

# Get a file with a predictable compression.
bztxt = test.support.findfile("lines.bz2")
with bz2.BZ2File(bztxt) as fpi:
    stuff = fpi.read()
    if not isinstance(stuff, bytes):
        raise TypeError

# Check multiple copies of decompressor.
multiple = b''
for i in range(10):
    c = bz2.BZ2Decompressor()
    multiple += c.decompress(stuff)
    c.decompress(b'')
    c.flush()
    c.close()

multiple = multiple.decode('ascii')
with open(test.support.findfile("lines.txt"), 'rt') as f:
    expected = f.read()
if not multiple.endswith(expected):
    raise ValueError

# Do one where the decompressor finishes with one call
