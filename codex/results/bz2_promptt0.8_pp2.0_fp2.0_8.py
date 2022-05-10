import bz2
# Test BZ2Decompressor.
decomp = bz2.BZ2Decompressor()
uncompressed = decomp.decompress(bz2_compressed)
print(uncompressed.decode('utf-8'))

# Test BZ2File.
uncompressed = []
with bz2.BZ2File('file.bz2', 'rb') as infile:
    for line in infile:
        uncompressed.append(line)
uncompressed = b''.join(uncompressed)
print(uncompressed.decode('utf-8'))

# Write compressed data to a file.
with open('file.bz2', 'wb') as outfile:
    outfile.write(bz2_compressed)

# Read compressed data from a file.
with bz2.BZ2File('file.bz2', 'rb') as infile:
    print(infile.read().decode('utf-8'))
</code>
The output is:
<code>Test data.
Test data.
Test data.
Test data.
</code
