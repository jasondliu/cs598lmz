import bz2
bz2.BZ2Compressor()

import bz2
bz2.BZ2Compressor(9)

import bz2
bz2.BZ2Compressor(compresslevel=9)

import bz2
bz2.BZ2Compressor(compresslevel=9, force=True)

import bz2
bz2.BZ2Compressor(compresslevel=9, force=True, small=True)

import bz2
bz2.BZ2Compressor(compresslevel=9, force=True, small=True).compress(b"abc")

import bz2
bz2.BZ2Compressor(compresslevel=9, force=True, small=True).flush()

import bz2
bz2.BZ2Compressor(compresslevel=9, force=True, small=True).compress(b"abc")
bz2.BZ2Compressor(compresslevel=9, force=True, small=True).flush()

import bz2
bz2.B
