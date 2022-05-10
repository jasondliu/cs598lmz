from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
```

```
#!/usr/bin/env python3

import sys
import lzma

if len(sys.argv) < 2:
    print('Usage: %s <archive.xz>' % sys.argv[0])
    sys.exit(1)

archive = sys.argv[1]

with lzma.open(archive) as f:
    for line in f:
        print(line.decode('utf-8').rstrip())
```

```
#!/usr/bin/env python3

import sys
import lzma

if len(sys.argv) < 2:
    print('Usage: %s <archive.xz>' % sys.argv[0])
    sys.exit(1)

archive = sys.argv[1]

with lzma.open(archive) as f:
    with open('output.txt', 'wb') as fo:
        while True:
            buf = f.read(1024)
            if not buf:
