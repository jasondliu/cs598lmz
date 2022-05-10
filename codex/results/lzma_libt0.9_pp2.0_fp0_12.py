import lzma
lzma.open.__doc__ = """open(name[, mode="r", format=LZMA_FORMAT_AUTO, ...])

Open an LZMA-compressed file in binary or text mode.

mode can be "r", "rb", "w", "wb", "x", "xb", "a" or "ab" for binary mode,
or "rt", "wt", "xt" or "at" for text mode.
The default mode is "rb".

For binary mode, this function is equivalent to the GzipFile class with
the first two arguments replaced by name and mode, and the filename argument
is wholly optional and not recommended.

For text mode, a GzipFile object is created, and wrapped in an
io.TextIOWrapper instance with the specified encoding.  Errors are handled
as described for the TextIOWrapper constructor.
"""

# gzip.py uses b"deflate" in places where it should be b"gzip".
import gzip
gzip._read_eof = gzip._read_eof2

# The bz2 module has a
