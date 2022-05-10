from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# $ python3 lzma_eof.py
# b'Hello World'
