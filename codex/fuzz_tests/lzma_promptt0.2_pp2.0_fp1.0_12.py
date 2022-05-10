import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress one chunk at a time
with open('lorem.xz', 'rb') as input, open('lorem.txt', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# Flush the decompressor to ensure that there's no data left
output.write(decompressor.flush())

# Decompress the whole file at once
with open('lorem.xz', 'rb') as f:
    file_content = decompressor.decompress(f.read())

# Decompress into a file-like object
with open('lorem.xz', 'rb') as input, open('lorem.txt', 'wb') as output:
    decompressor.decompress(input.read(), max_length=1024, output=output)

# Decompress into a bytearray
with open
