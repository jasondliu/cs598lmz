import lzma
lzma.__doc__ = """\
LZMA compressor/decompressor.\n\
\n\
This module provides a compatible interface to the lzma library by\n\
Laurence A. G. Cannon.\n\
\n\
Commonly used methods:\n\
\n\
decompress(data, format=FORMAT_AUTO, memlimit=None, filters=None)\n\
    Decompresses the data.\n\
\n\
compress(data, format=FORMAT_AUTO, check=-1, preset=None, filters=None)\n\
    Compresses the data.\n\
\n\
encode(data, format=FORMAT_AUTO, check=-1, preset=None, filters=None)\n\
    Compresses the data and returns a bytearray object.\n\
\n\
decode(data, format=FORMAT_AUTO, memlimit=None, filters=None)\n\
    Decompresses the data and returns a bytearray object.\n\
\n\
FORMAT
