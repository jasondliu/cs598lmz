from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# $ python3 lzma_decompress.py
# b'This is the original text.'

# $ python3 lzma_decompress.py
# b'This is the original text.'
