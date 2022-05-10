from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

import bz2
bz2.decompress(bz2_data)
```

## AES (Advanced Encryption Standard)

AES is a symmetric block cipher chosen by the U.S. government to protect classified information and is implemented in software and hardware throughout the world to encrypt sensitive data. Unlike its predecessors, DES and 3DES, AES does not use a Feistel network.

In Python, you may use `Crypto.Cipher` to encrypt or decrypt files using AES.

### Example

```python
from Crypto.Cipher import AES
from Crypto import Random
from os import urandom

key = urandom(16)
iv = Random.new().read(16)

cipher = AES.new(key, AES.MODE_CBC, iv)

msg = cipher.encrypt(b'Hello, world!')
print(msg)

decrypt = AES.new(key, AES.MODE_CBC, iv)
print(decrypt.decrypt(msg))
```

## RSA (Rivest-Shamir
