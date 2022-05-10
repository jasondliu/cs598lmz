import lzma
lzma.decompress(data)

# decompress the data to a file-like object
with lzma.open(data) as f:
    f.read()

# use lzma.open with a filename
with lzma.open("file.xz") as f:
    f.read()

# use lzma.open with a filename and explicit mode
with lzma.open("file.xz", "rt") as f:
    f.read()

# use lzma.open with a filename and explicit mode and encoding
with lzma.open("file.xz", "rt", encoding="utf-8") as f:
    f.read()

# use lzma.open with a filename, explicit mode, and filters
with lzma.open("file.xz", "rt", filters=[{"id": lzma.FILTER_LZMA2, "preset": 3}]) as f:
    f.read()

# use lzma.open with a filename, explicit mode, encoding, and filters
with lzma.
