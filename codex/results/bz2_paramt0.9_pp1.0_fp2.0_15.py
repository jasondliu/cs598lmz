from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(junk_data)

import gzip
gzip.decompress(junk_data)

import zipfile
zipfile.ZipFile(io.BytesIO(junk_data)).infolist()
import lzma
lzma.open(io.BytesIO(junk_data)).infolist()


lzma.open(io.BytesIO(junk_data), format=lzma.FORMAT_ALONE).infolist()
lzma.open(io.BytesIO(junk_data), format=lzma.FORMAT_RAW).infolist()


def bz2_filter(stream):
    for chunk in iter(lambda: stream.read(io.DEFAULT_BUFFER_SIZE), b""):
        yield BZ2Decompressor().decompress(chunk)

with lzma.open(io.BytesIO(junk_data), format=lzma.FORMAT_RAW, filters=[{"id": lzma.FILTER_LZMA2, "preset": 9 | lzma
