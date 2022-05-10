import lzma
lzma.decompress(data)

# base64
import base64
base64.b64decode(data)

# rot-13
import codecs
codecs.decode(data, 'rot_13')
```

### XOR
```python
# XOR
def xor(data, key):
    l = len(key)
    return bytearray((
        (data[i] ^ key[i % l]) for i in range(0,len(data))
    ))

# XOR brute force
def xor_brute_force(data):
    for i in range(256):
        key = chr(i)
        result = xor(data, key)
        print(key, result)
```

### AES
```python
# AES
from Crypto.Cipher import AES
import base64
import os

def decrypt_aes(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(data))

def encrypt_
