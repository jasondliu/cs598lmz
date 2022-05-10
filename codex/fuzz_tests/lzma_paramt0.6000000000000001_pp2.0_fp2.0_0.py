from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed).decode("utf-8")

# bz2
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed).decode("utf-8")

# zlib
import zlib
zlib.decompress(compressed, wbits=31).decode("utf-8")
```

## License

[MIT](https://github.com/sindresorhus/decompress-cli/blob/master/license) © [Sindre Sorhus](https://sindresorhus.com)
