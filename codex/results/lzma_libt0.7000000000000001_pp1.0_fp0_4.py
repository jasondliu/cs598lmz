import lzma
lzma.LZMADecompressor().decompress(f.read())

# This is the end of the file
f.read()
b''

# And this also
f.read1(10)
b''

# Running out of data while trying to decompress produces
# EOFError, just like the zlib module.
f = io.BytesIO(b"garbage")
lzma.LZMADecompressor().decompress(f.read())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.8/lzma.py", line 329, in decompress
    return self.decompressobj.decompress(data)
  File "/usr/lib/python3.8/lzma.py", line 296, in decompress
    raise EOFError("Compressed file ended before the "
EOFError: Compressed file ended before the end-of-stream marker was reached

# Trying to decompress data not produced by LZMA.COMPRESS produces
