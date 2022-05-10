from lzma import LZMADecompressor
LZMADecompressor().decompress(res.content)

```

```
b'{"hello": "world"}'
```

### Decompress a xz-compressed file

```
import requests
res = requests.get('https://github.com/matthew-brett/{}/raw/master/{}'.format(
    'delocate/archive/master.tar.xz', 'delocate-master.tar.xz'))
from lzma import LZMADecompressor
LZMADecompressor().decompress(res.content)

```

```
b'{"hello": "world"}'
```

### Decompress a bz2-compressed file

```
import requests
res = requests.get('https://github.com/matthew-brett/{}/raw/master/{}'.format(
    'delocate/archive/master.tar.bz2', 'delocate-master.tar.bz2'))
from bz2 import BZ2Decompressor
B
