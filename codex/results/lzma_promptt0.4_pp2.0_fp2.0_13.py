import lzma
# Test LZMADecompressor

# Create an LZMADecompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('compressed_file.xz', 'rb') as input, open('uncompressed_file', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        result = decompressor.decompress(chunk)
        if result:
            output.write(result)
        else:
            break

# Read all at once
with open('compressed_file.xz', 'rb') as input, open('uncompressed_file', 'wb') as output:
    result = decompressor.decompress(input.read())
    output.write(result)

# Read into a buffer
buf = bytearray(1024)
with open('compressed_file.xz', 'rb') as input, open('uncompressed_file', 'wb') as output:
    while True:
        chunk = input.read(1024)

