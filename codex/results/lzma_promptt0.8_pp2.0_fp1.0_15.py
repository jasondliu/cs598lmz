import lzma
# Test LZMADecompressor.eof
BUG_LZMA_EOF = lzma.LZMAError.EOS != lzma.LZMA_RESULT_EOS

import socket
# Test socket.recv.__doc__ for mention of 'buffering'
BUG_SOCKET_RECV_BUFFERING = 'buffering' not in socket.recv.__doc__

import struct
# Test struct.pack.__doc__ for mention of 'native byte order'
BUG_STRUCT_PACK_NATIVE_BYTE_ORDER = 'native byte order' not in struct.pack.__doc__

import sys
# Test sys.platform
BUG_SYS_PLATFORM_DARWIN = sys.platform == 'darwin'

import textwrap
# Test textwrap.TextWrapper to see whether it implements break_on_hyphens
BUG_TEXTWRAP_BREAK_ON_HYPHENS = not hasattr(textwrap.TextWrapper, 'break_on_hyphens')

import time
# Test time.sleep() for rounding behavior
BUG_TIME_SLEEP_
