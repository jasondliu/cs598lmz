import lzma
# Test LZMADecompressor.
# Create an LZMADecompressor object.
with lzma.open('python.xz', 'rb') as f:
    file_content = f.read()
    print(file_content)
