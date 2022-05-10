import bz2
bz2.compress()
```

```python
import zlib
zlib.compress()
```

压缩文件：
```python
import bz2
f = bz2.BZ2File('file.bz2', 'wb')
f.write(bytes)
f.close()
```

读取文件：
```python
import bz2
f = bz2.BZ2File('file.bz2', 'rb')
bytes = f.read()
f.close()
```

## 其他编码

### base64编码

base64编码是一种任意二进制到文本字符串的编码方法。

base64编码的长度总是比原始二进制数据
