from lzma import LZMADecompressor
LZMADecompressor.check_size = (lambda x,y: None)
