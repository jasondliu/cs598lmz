from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# gzip
from gzip import decompress
decompress(data)

# zlib
import zlib
zlib.decompress(data, -zlib.MAX_WBITS)
```

## References

- [The Brotli Compressed Data Format](https://tools.ietf.org/html/rfc7932)
- [Brotli Compressed Data Format](https://www.w3.org/TR/brotli/)
- [The Zopfli Compression Algorithm](https://github.com/google/zopfli)
- [Brotli](https://github.com/google/brotli)
- [Zopfli](https://github.com/google/zopfli)
- [Brotli](https://github.com/google/brotli)
- [Zopfli](https://github.com/google/zopfli)
- [Brotli](https://github.com/google/brotli)
- [Zopfli](https://github.com/
