import lzma
# Test LZMADecompressor
import _lzma
from _lzma import LZMADecompressor

d = LZMADecompressor()
assert d.decompress(b"") == b""
assert d.decompress(b"\x00\x00\x00\x00") == b""
assert d.decompress(b"\x00\x00\x00\x00" * 2) == b""
assert d.decompress(b"\x00\x00\x00\x00" * 10) == b""
assert d.decompress(b"\x00\x00\x00\x00" * 100) == b""
assert d.decompress(b"\x00\x00\x00\x00" * 1000) == b""

assert d.decompress(b"\x00\x00\x00\x00" * 1000 + b"\x00") == b""
assert d.decompress(b"\x00\x00\x00\x00" * 1000 + b"\x00",
