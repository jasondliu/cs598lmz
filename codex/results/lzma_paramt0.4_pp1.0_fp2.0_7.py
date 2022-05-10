from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# decompress with zlib
from zlib import decompress
decompress(data)

# decompress with bz2
from bz2 import decompress
decompress(data)

# decompress with gzip
from gzip import decompress
decompress(data)

# decompress with brotli
from brotli import decompress
decompress(data)

# decompress with lz4
import lz4.block
lz4.block.decompress(data)

# decompress with snappy
import snappy
snappy.decompress(data)
```

## License

MIT
