from lzma import LZMADecompressor
LZMADecompressor().decompress(b'YXNjYXZlCg==')

'ascii'

LZMADecompressor().decompress(b'YXNjYXZlCg==', max_length=4)

'asci'

LZMADecompressor().decompress(b'YXNjYXZlCg==', max_length=2)

'as'

LZMADecompressor().decompress(b'YXNjYXZlCg==', max_length=4)

'asci'

LZMADecompressor().decompress(b'YXNjYXZlCg==', max_length=2)

'as'

LZMADecompressor().decompress(b'YXNjYXZlCg==', max_length=None)

'ascii'

LZMADecompressor().decompress(b'YXNjYXZlCg==', max_length
