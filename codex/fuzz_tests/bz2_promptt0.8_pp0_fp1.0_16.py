import bz2
# Test BZ2Decompressor
bz2c = bz2.BZ2Decompressor()

#Test bz2 decompression
bz2c.decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59')

#Test bz2 decompression after initial bytes
bz2c.decompress(b'\x17\x72\x45\x38\x50\x90\x00\x00\x00\x00\x00\x01')
# Test BZ2Compressor
# Create data to compress
data = b'UNCOMPRESSED\n'
bz2c = bz2.BZ2Compressor()

# Compress 1
bz2c.compress(data)

# Compress 2
bz2c.compress(data)

# Finish compression
bz2c.flush()
# Read data from a compressed file
import bz2, os
os.chdir(r'C:\Users\Zizhao Zhang\Desktop\python4
