from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)
# b'secret message'
```

### Кодирование и декодирование Base64

```python
from base64 import b64encode, b64decode
b64encode(b'binary\x00string')
# b'YmluYXJ5AHN0cmluZw=='
b64decode(b'YmluYXJ5AHN0cmluZw==')
# b'binary\x00string'
```

Для работы с ASCII-кодированными текстовыми данными вместо байтов можно использовать класс `base64.b64encode()` и `base64.b64decode()`

