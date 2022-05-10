import bz2
# Test BZ2Decompressor.eof for a file which has an odd number of nulls

data = bz2.BZ2Compressor().compress(b"\0" * 3)
data += bz2.compress(b"x")

decomp = bz2.BZ2Decompressor()
assert decomp.decompress(data) == b"\0" * 3
assert not decomp.eof
assert decomp.decompress(bz2.compress(b"y")) == b"y"
assert decomp.eof
# issue #10870: BZ2Decompressor.read has a hardcoded 32MiB block size,
# which may be insufficient for extremely long lines.
import bz2
import contextlib
import io
import itertools

long_line = "".join(str(i).encode("ascii") for i in itertools.count())
compressed = bz2.compress(long_line[:0x40000]) # 256KiB

with contextlib.closing(bz2.BZ2Decompressor()) as decomp:
