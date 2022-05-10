from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# bz2
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# zlib
import zlib
zlib.decompress(data)
```

## 参考

- [Pythonで圧縮・解凍する方法](https://qiita.com/kakiuchis/items/a5c8e0a5f5c4b4d4e4c8)
- [Pythonでzipファイルを解凍する方法](https://qiita.com/kakiuchis/items/a5c8e0a5f5c4b4d4e4c8#zipファイルを解凍する)
- [Pythonでtarファイルを解凍する方法](https://qiita.com/kakiuchis/items/a5c8e0a5f5c4b4d4e4c8#tarファイル
