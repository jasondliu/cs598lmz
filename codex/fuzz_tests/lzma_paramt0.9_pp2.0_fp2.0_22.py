from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO).decompress(info.get_lzma())
```

```CONFORMANT``` and ```RAW``` constants are for compatibility with the
```lzma``` module.

Decompression from any file or stream is supported.  The stream may be read at
once or block-by-block, and may have arbitrary length.

```py
from lzma import LZMADecompressor
# The recommended compression format, which is not supported in the stdlib
FILTER_LZMA1 = 1
with open(filename, 'rb') as f:
    LZMADecompressor(format=FORMAT_RAW, filters=[{'id': FILTER_LZMA1}]).decompress(f)
```

## Documentation

The documentation is also available on [readthedocs.org](https://python-lzma.readthedocs.org).

## Release history

* 2017-12-09: Version 0.4.9
   * Fixed failing functional tests on certain combinations of PyPy
