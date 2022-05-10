import bz2
# Test BZ2Decompressor and BZ2Compressor

## Stream

fd = open('/etc/passwd', 'rb')
c = bz2.BZ2Compressor()
d = bz2.BZ2Decompressor()

while True:
    block = fd.read(64)
    if len(block) == 0: break
    print('{} -> {}'.format(len(block), len(c.compress(block))))
    print('{} -> {}'.format(len(c.compress(block)), len(d.decompress(c.compress(block)))))

## Compress and Decompress

fd = open('/etc/passwd', 'rb')
compressed = bz2.compress(fd.read())
print('{} -> {}'.format(len(fd.read()), len(compressed)))

fd.close()

fd = open('/etc/passwd', 'rb')
decompressed = bz2.decompress(compressed)
