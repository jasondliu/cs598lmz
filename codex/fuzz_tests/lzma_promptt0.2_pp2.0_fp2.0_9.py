import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress one chunk at a time
with open('data/compressed_sample.xz', 'rb') as input:
    with open('data/decompressed_sample.txt', 'wb') as output:
        while True:
            chunk = input.read(1024)
            if not chunk:
                break
            result = decompressor.decompress(chunk)
            if result:
                output.write(result)
            else:
                break
        output.write(decompressor.flush())
 
# Decompress the whole file at once
with open('data/compressed_sample.xz', 'rb') as input:
    with open('data/decompressed_sample.txt', 'wb') as output:
        output.write(decompressor.decompress(input.read()))
 
# Decompress a stream of data
with open('data/compressed_sample.xz', 'rb') as input:
    with open('data
