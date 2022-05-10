import lzma
lzma.open('file.xz')
```

## bz2

```python
import bz2
bz2.open('file.bz2')
```

## gzip

```python
import gzip
gzip.open('file.gz')
```

## tar

```python
import tarfile
tarfile.open('file.tar')
```

## zip

```python
import zipfile
zipfile.open('file.zip')
```

## 读取压缩文件的内容

```python
import gzip
with gzip.open('file.gz', 'rt') as f:
    text = f.read()
```

## 从字符串中读取

```python
import io
s = io.StringIO('Hello\nWorld\n')
```

## 从字节串中读取

```python
import io
s =
