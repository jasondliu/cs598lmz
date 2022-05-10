import bz2
bz2.decompress(data)

# Create the decompression object
decompressor = bz2.BZ2Decompressor()

# Decompress the data
decompressor.decompress(data)

# Finish decompression
decompressor.flush()

# Decompress an entire file
with open('file.bz2', 'rb') as input:
    with open('file.out', 'wb') as output:
        while True:
            chunk = input.read(100000)
            if not chunk:
                break
            output.write(decompressor.decompress(chunk))
        output.write(decompressor.flush())

# Compress an entire file
with open('file.txt', 'rb') as input:
    with bz2.open('file.bz2', 'wb') as output:
        while True:
            chunk = input.read(100000)
            if not chunk:
                break
            output.write(chunk)

# Compress data iteratively
import bz2
compressor = bz2.
