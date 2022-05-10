import bz2
# Test BZ2Decompressor with a string
data = bz2.compress(b"testing")
decompressor = bz2.BZ2Decompressor()
orig = decompressor.decompress(data)
print(orig)

# Test BZ2Decompressor with a file
output = io.BytesIO()
decompressor = bz2.BZ2Decompressor()
with bz2.open('data.txt.bz2', 'rb') as input:
    for block in iter(lambda : input.read(100 * 1024), b''):
        output.write(decompressor.decompress(block))

print(output.getvalue())
 
# Test BZ2Decompressor with an incremental decompress
d = bz2.BZ2Decompressor()
compressed = d.compress(b'x' * 10)
compressed += d.compress(b'y' * 10)
compressed += d.flush()
uncompressed = d.decompress(compressed)
print(uncompressed)
assert len(uncompressed) == 20

