from lzma import LZMADecompressor
LZMADecompressor()

from lzma import compress, decompress

compress(b"foo")
decompress(b"\x5d\x00\x00\xff\xff\x04\x00\x02\xff\xff\xff\xff\xff\xff")

from lzma import open

open(__file__, "w")
open(__file__, "rb")
open(__file__, "rb", preset=9 | LZMA_PRESET_EXTREME)
open(__file__, "rb", filters=[{"id": LZMA_FILTER_LZMA1, "preset": 9 | LZMA_PRESET_EXTREME}])
open(__file__, "rb", filters=[{"id": LZMA_FILTER_LZMA1, "preset": 9 | LZMA_PRESET_EXTREME}])
open(__file__, "rb", encoding="utf-8")

""" + _make_test_data(b"foo") + """

with open(__file__, "rb") as f:
