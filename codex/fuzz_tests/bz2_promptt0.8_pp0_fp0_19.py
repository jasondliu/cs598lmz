import bz2
# Test BZ2Decompressor by reading the output of BZ2Compressor
# incrementally, one line at a time.

c = bz2.BZ2Compressor()
uncompressed_data = b'abcdefghijklmnopqrstuvwxyz'
compressed_data = c.compress(uncompressed_data) + c.flush()

d = bz2.BZ2Decompressor()
lines = []
for line in compressed_data.splitlines(True):
    lines.append(d.decompress(line))

output = b''.join(lines)
assert output == uncompressed_data

print(lines)
print(output)
