import bz2
# Test BZ2Decompressor and BZ2Compressor

# See http://wiki.python.org/moin/Bz2File for details

# Test decompressor
decompressor = bz2.BZ2Decompressor()

# Test compressor
compressor = bz2.BZ2Compressor()

# Read data from a file
f = open('/usr/share/doc/python2.7/examples/Tools/i18n/pygettext.py', 'rb')
data = f.read()
f.close()

# Compress data
compressed = compressor.compress(data) + compressor.flush()

# Decompress data
decompressed = decompressor.decompress(compressed)

# Print the size of data, compressed and decompressed
print len(data), len(compressed), len(decompressed)

# Check that decompressed data is the same as original data
print decompressed == data
