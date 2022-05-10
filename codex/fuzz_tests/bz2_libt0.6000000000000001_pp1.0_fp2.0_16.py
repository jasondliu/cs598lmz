import bz2
bz2.BZ2File(filename).readlines()

```

```python
import gzip
with gzip.open(filename, 'rt') as f:
    lines = f.readlines()
```

```python
import lzma
with lzma.open(filename, 'rt') as f:
    lines = f.readlines()
```

## 读取二进制文件

```python
with open('somefile.bin', 'rb') as f:
    data = f.read()
```

```python
with open('somefile.gz', 'rb') as f:
    data = f.read()
```

## 读取文本文件的行

```python
with open(filename) as f:
    for line in f:
        print(line, end='')
```

```python
with open(filename) as f:
    lines = (line for line in f if not line.startswith('#
