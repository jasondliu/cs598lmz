from lzma import LZMADecompressor
LZMADecompressor.decompress(data)
```

```
b'Hello, world!'
```

## Compress a file

```python
from lzma import LZMAFile
with LZMAFile('file.xz', 'w') as f:
    f.write(b'Hello, world!')
```

## Decompress a file

```python
from lzma import LZMAFile
with LZMAFile('file.xz', 'r') as f:
    print(f.read())
```

```
b'Hello, world!'
```

## Compress and decompress a file using a single command

```python
from lzma import compress, decompress
compress('file.xz', 'file')
decompress('file.xz', 'file.out')
```

## Compress a file using a preset

```python
from lzma import LZMAFile
with LZMAFile('file.xz', 'w', preset=9) as f:
    f.
