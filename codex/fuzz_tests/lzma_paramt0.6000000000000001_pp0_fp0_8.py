from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# ...

import bz2
bz2.decompress(data)

# ...

import zlib
zlib.decompress(data)
```

### Encryption

```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message. Not for prying eyes.")
f.decrypt(token)
```

### Hash

```python
from hashlib import sha1
sha1(data).hexdigest()

from hashlib import sha256
sha256(data).hexdigest()

from hashlib import md5
md5(data).hexdigest()
```

### Regex

```python
import re
re.findall(r'\b\w{5,6}\b', data)
re.findall(r'(?:\w{2,4})(?:\s)(?:\w{2,4})', data)

