import lzma
# Test LZMADecompressor

d = lzma.LZMADecompressor()

# Decompress a file
with open('test.xz', 'rb') as f:
    decompressed_data = d.decompress(f.read())

# Decompress a stream
with open('test.xz', 'rb') as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        decompressed_data = d.decompress(chunk)
        if decompressed_data:
            print(decompressed_data)

# Decompress a stream in chunks
with open('test.xz', 'rb') as f:
    while True:
        chunk = f.read(1024)
        if not chunk:
            break
        for data in d.decompress(chunk, max_length=16):
            print(data)

# Decompress a stream in chunks with a maximum amount of data to return
with open('test.xz', 'rb') as f:
    while True:
        chunk = f.
