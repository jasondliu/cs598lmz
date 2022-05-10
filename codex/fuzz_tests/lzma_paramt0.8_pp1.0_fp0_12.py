from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self: b''
def decompress(data):
    return LZMADecompressor().decompress(data)

_version                = '0021'
_compression_threshold  = 1024*512
# _version                = '0018'
# _compression_threshold  = 1024*1024

# Based on:
# https://stackoverflow.com/questions/3288595/multiprocessing-how-to-use-pool-map-on-a-function-defined-in-a-class

if sys.version >= '3':
    buffer = memoryview
    def tobytes(x):
        return bytes(x) if isinstance(x, buffer) else bytes(x, 'latin1')
    def frombytes(x):
        return x if isinstance(x, buffer) else x.encode('latin1')
else:
    def tobytes(x):
        return buffer(x)
    def frombytes(x):
        return buffer(x)


class Dict(dict):
    """
    Dict
