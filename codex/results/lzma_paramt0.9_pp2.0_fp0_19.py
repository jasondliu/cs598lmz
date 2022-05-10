from lzma import LZMADecompressor
LZMADecompressor().decompress(open(chrome.filename, 'rb').read())
# b'This is the chrome file How to use lzma to open'
