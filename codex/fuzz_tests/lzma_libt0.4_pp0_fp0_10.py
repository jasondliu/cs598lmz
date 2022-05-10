import lzma
lzma.decompress(data)

# 压缩
lzma.compress(data)
```

### bz2

```python
import bz2
bz2.decompress(data)

# 压缩
bz2.compress(data)
```

### zlib

```python
import zlib
zlib.decompress(data)

# 压缩
zlib.compress(data)
```

### zipfile

```python
import zipfile

# 压缩
z = zipfile.ZipFile('test.zip', 'w')
z.write('test.txt')
z.close()

# 解压
z = zipfile.ZipFile('test.zip', 'r')
z.extractall()
z.close()
```

### tarfile

```python
import tarfile

# 压缩
t = tarfile.open('test.tar', 'w')
t.add('test
