import lzma
# Test LZMADecompressor

with lzma.open('file.xz') as f:
    file_content = f.read()

decompressor = lzma.LZMADecompressor()
