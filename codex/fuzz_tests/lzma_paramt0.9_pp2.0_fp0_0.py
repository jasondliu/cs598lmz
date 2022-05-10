from lzma import LZMADecompressor
LZMADecompressor().decompress(b"\x00\x01\x02")

# extraction
import json
from bz2 import BZ2File

def bz2_decode(file):
    with BZ2File(file) as f:
        data = f.read()
    return data.decode("utf-8")

def json_loads(data):
    return json.loads(data)

def process(file):
    data = bz2_decode(file)
    data = json_loads(data)
    return data

file = "ch04-data/py3/data.json.bz2"
process(file)
```

### 3.5.5 更多关于网络和系统编程的信息

#### 3.5.5.1 正则表达式

```python
# socket
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_
