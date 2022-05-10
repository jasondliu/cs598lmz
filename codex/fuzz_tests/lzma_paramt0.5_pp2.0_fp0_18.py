from lzma import LZMADecompressor
LZMADecompressor.__module__ = 'lzma'

# Get the lzma library name
_lzma = ctypes.util.find_library('lzma')

# Load the lzma library
if _lzma:
    _lzma = ctypes.CDLL(_lzma)
else:
    raise OSError('lzma library not found')

# Set up the lzma library function arguments
_lzma.lzma_stream_buffer_decode.argtypes = [
    ctypes.POINTER(lzma_stream), ctypes.c_void_p, ctypes.c_size_t,
    ctypes.c_void_p, ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t
]

# Set up the lzma library function return types
_lzma.lzma_stream_buffer_decode.restype = lzma_ret

# Set up the lzma library function arguments
_lzma.lzma_auto_
