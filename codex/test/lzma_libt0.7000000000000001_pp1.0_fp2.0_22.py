import lzma
lzma.decompress(lzma.compress(b"Hello World"))

# Python 2.7.9 introduced per-file compression in the zipfile module.
import zipfile
