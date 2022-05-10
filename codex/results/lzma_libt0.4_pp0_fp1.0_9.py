import lzma
lzma.decompress(open('/tmp/backup.lzma', 'rb').read())

# decompress bz2
import bz2
bz2.decompress(open('/tmp/backup.bz2', 'rb').read())

# decompress gzip
import gzip
gzip.decompress(open('/tmp/backup.gz', 'rb').read())

# decompress zlib
import zlib
zlib.decompress(open('/tmp/backup.zlib', 'rb').read())
```

### Encrypt/Decrypt

```python
# encrypt
import base64
import hashlib
import os
import random
import string

from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key, filename):
    chunksize = 64 * 1024
    outputFile = filename + ".enc"
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = ''

    for i in range(16):
        IV += chr(random.
