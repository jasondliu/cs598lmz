import lzma
lzma.decompress(s)

s = b'\x00\x10\x00\x00'
import snappy
snappy.decompress(s)

s = b'\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00'
import zstandard
zstandard.ZstdDecompressor().decompress(s)

s = b'\xfd\xb5\x2c\x27\x0a\x00\x00\x00'
brotli.decompress(s)

s = b'\x03\x00\x00\x00'
blosc.decompress(s)

s = b'\x01\x11\x00\x00\x0a\x00\x00\x00'
import zlib
zlib.decompress(s)
