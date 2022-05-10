from lzma import LZMADecompressor
LZMADecompressor().decompress(file.read(1200000))
```

```python
In [1]: import lzma
In [2]: file = open("../../Downloads/output.lzma", "rb")
In [3]: decompressor = lzma.LZMADecompressor()
In [4]: decompressor.decompress(file.read(100000))
Out[4]: b''
In [5]: open("test.txt", "w").write(decompressor.decompress(file.read(7640000)))
In [6]: open("test.txt", "w").write(decompressor.decompress(file.read(7640000)))
In [7]: open("test.txt", "w").write(decompressor.decompress(file.read()))
```


```python
import json
a = json.load(open("test.txt"))
```


```python
import pandas as pd
df = pd.DataFrame.from_records(a)
df.shape
df.head()

