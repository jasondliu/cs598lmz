import bz2
bz2.decompress(alice_compressed)
 
 
# How many bytes are given back by the decompressor?
len(bz2.decompress(alice_compressed))

# What is the compression ratio?
compression_ratio = len(alice_compressed) / len(alice_raw)
print(compression_ratio)

# What is the decompression time?
import time
start = time.time()
bz2.decompress(alice_compressed)
end = time.time()
execution_time = end - start
print(execution_time)

# What is the compression time?
start = time.time()
len(bz2.compress(alice_raw))
end = time.time()
execution_time = end - start
print(execution_time)

# Compression ratio of gzip
import gzip
alice_compressed = gzip.compress(alice_raw)
compression_ratio = len(alice_compressed) / len(alice_raw)

