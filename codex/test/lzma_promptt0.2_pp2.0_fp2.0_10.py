import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()

data = b"Hello world!"
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

print(decompressed)

# Test LZMAFile

with lzma.open("hello.xz", "w") as f:
    f.write(b"Hello world!")

with lzma.open("hello.xz", "r") as f:
    file_content = f.read()

print(file_content)

# Test LZMAError

try:
    decompressor = lzma.LZMADecompressor()
    decompressor.decompress(b"garbage")
except lzma.LZMAError as e:
    print("Error: {}".format(e))

# Test LZMAFilter

