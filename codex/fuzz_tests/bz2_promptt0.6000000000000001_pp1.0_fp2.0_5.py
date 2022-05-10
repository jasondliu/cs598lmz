import bz2
# Test BZ2Decompressor
bz2_comp = bz2.BZ2Decompressor()
bz2_comp.decompress(bz2_data)
# Test BZ2File
bz2_file = bz2.BZ2File("python_tutorial.bz2")
bz2_file.read()
bz2_file.seek(0)

# Gzip
import gzip
# Test GzipFile
gzip_file = gzip.GzipFile("python_tutorial.gz")
gzip_file.read()
gzip_file.seek(0)
# Test GzipFile
gzip_file = gzip.GzipFile("python_tutorial.gz", "wb")
gzip_file.write(data)
gzip_file.close()

# Compress data in memory
import zlib
zlib.compress(data)
zlib.decompress(zlib.compress(data))

# Test compression level
zlib.compress(data, 1)
zlib.compress(data, 9)

# Test
