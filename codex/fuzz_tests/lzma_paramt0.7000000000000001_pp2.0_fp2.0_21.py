from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
```

```
# I know you'll love this one ;)
from zlib import decompress
decompress(data)
```

```
# This is it!
from bz2 import decompress
decompress(data)
```
