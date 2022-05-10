from lzma import LZMADecompressor
LZMADecompressor.__doc__ = '''
LZMA decompressor.

This decompressor supports the LZMA format, which is used by the
XZ compression format.

The decompressor can be used in one of two ways:

* As a stream filter; in this mode, the data to be decompressed is
  written to the decompressor object, and the uncompressed data is
  read from the object.
* As a one-shot decompressor; in this mode, the data to be
  decompressed is given to the decompressor object as a bytes-like
  object, and the decompressed data is returned as a bytes object.

Stream filter usage:

    >>> d = LZMADecompressor()
    >>> with open('test.xz', 'rb') as f:
    ...     for chunk in iter(lambda: f.read(1024), b''):
    ...         data = d.decompress(chunk)
    ...         if data:
    ...             sys.stdout.write(data)
    ...     sys.stdout.write(d.flush())

One-shot usage:


