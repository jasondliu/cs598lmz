import bz2
# Test BZ2Decompressor
bz2.BZ2Decompressor()

import zlib
# Test ZlibDecompressor
zlib.decompressobj()

import lzma
# Test LZMADecompressor
lzma.LZMADecompressor()

import sys
# Test sys.getsizeof()
sys.getsizeof(1)

import mmap
# Test mmap.mmap()
mmap.mmap(-1, 0)

import signal
# Test signal.siginterrupt()
signal.siginterrupt(signal.SIGINT, True)
# Test signal.set_wakeup_fd()
signal.set_wakeup_fd(1)

import curses
# Test curses.initscr()
curses.initscr()

import locale
# Test locale.setlocale()
locale.setlocale(locale.LC_ALL, '')

import struct
# Test struct.pack_into()
struct.pack_into('i', b'', 0, 0)

import time
# Test time.
