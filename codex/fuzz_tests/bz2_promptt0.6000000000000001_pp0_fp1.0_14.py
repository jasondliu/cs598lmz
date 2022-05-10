import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
decompressed_data = d.decompress(compressed_data)
decompressed_data

# Test BZ2File
with bz2.BZ2File('compressed_file.bz2', 'wb') as f:
    f.write(data)

with bz2.BZ2File('compressed_file.bz2', 'rb') as f:
    decompressed_data = f.read()
decompressed_data

# Gzip
import gzip
# Test GzipFile
with gzip.GzipFile('compressed_file.gz', 'wb') as f:
    f.write(data)

with gzip.GzipFile('compressed_file.gz', 'rb') as f:
    decompressed_data = f.read()
decompressed_data

# Test gzip
compressed_data = gzip.compress(data)
compressed_data

decompressed_data = gzip.decompress(compressed_data)
dec
