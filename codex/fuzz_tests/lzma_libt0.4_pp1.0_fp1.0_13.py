import lzma
lzma.decompress(b'\x00')

# -------------------------------------------------------------------

import lzma
lzma.decompress(b'\x00', format=lzma.FORMAT_AUTO)

# -------------------------------------------------------------------

import lzma
lzma.decompress(b'\x00', format=lzma.FORMAT_XZ)

# -------------------------------------------------------------------

import lzma
lzma.decompress(b'\x00', format=lzma.FORMAT_ALONE)

# -------------------------------------------------------------------

import lzma
lzma.decompress(b'\x00', format=lzma.FORMAT_RAW)

# -------------------------------------------------------------------

import lzma
lzma.decompress(b'\x00', format=lzma.FORMAT_UNKNOWN)

# -------------------------------------------------------------------

import lzma
lzma.decompress(b'\x00', check=-1)

# -------------------------------------------------------------------

import lzma
lzma.decompress(b'\x
