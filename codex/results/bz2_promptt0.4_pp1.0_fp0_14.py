import bz2
# Test BZ2Decompressor

# https://docs.python.org/3/library/bz2.html
decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f:
    compressed_data = f.read()

# Decompress data
data = decompressor.decompress(compressed_data)

# Print decompressed data
print(data)

# Print decompressed data
print(data.decode())

# Print decompressed data
print(data.decode('utf-8'))

# Print decompressed data
print(data.decode('utf-8').strip())

# Print decompressed data
print(data.decode('utf-8').strip().split())

# Print decompressed data
print(data.decode('utf-8').strip().split()[:10])

# Print decompressed data
print(data.decode('utf-8').strip().split()[:10][0])

# Print decompressed data
print(data.decode('utf-8').strip().split
