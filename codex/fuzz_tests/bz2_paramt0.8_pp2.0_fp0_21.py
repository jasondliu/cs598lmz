from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(c)

```

### 压缩文件

```
import bz2
import os

os.chdir('/tmp')
data = open('/tmp/lorem.txt', 'rb').read()
print('%d bytes before compression' % len(data))
compressed = bz2.compress(data)
print('%d bytes after compression' % len(compressed))

```

### 压缩文件2

```
import bz2
import os

os.chdir('/tmp')
data = open('/tmp/lorem.txt', 'rb').read()
print('%d bytes before compression' % len(data))
compressed = bz2.compress(data)
print('%d bytes after compression' % len(compressed))

open('/tmp/lorem.txt.bz2', 'wb').write(compressed)

```

### 解压文件

```
import bz2

original
