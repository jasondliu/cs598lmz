import bz2
# Test BZ2Decompressor
decompressor = BZ2Decompressor()

# Read compressed data from a file, and feed each chunk into the decompressor
with open('enwik8_bz2', 'rb') as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        decompressed_data += decompressor.decompress(chunk)

print(decompressed_data)

print(len(decompressed_data))

print(len(data))


# Read a gzip compressed file
import gzip
with gzip.open('sample.txt.gz') as f:
    sample_data = f.read()

print(sample_data)

# Alternatively, you can use GzipFile directly
import gzip
with open('sample.txt.gz', 'rb') as f:
    with gzip.GzipFile(fileobj=f) as decompressed_f:
        sample_data = decompressed_f.read()

print(sample_data)

# Compress data using gzip
import gzip
uncomp
