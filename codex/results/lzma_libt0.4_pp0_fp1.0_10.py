import lzma
lzma.decompress(data)

# 'Hello World!'
```

## LZMA2

LZMA2 is a variant of LZMA that supports multiple data chunks.

```python
import lzma
lzma.decompress(data, format=lzma.FORMAT_ALONE)

# 'Hello World!'
```

## XZ

XZ is a format that uses the LZMA2 algorithm.

```python
import lzma
lzma.decompress(data, format=lzma.FORMAT_XZ)

# 'Hello World!'
```

## LZMA Utils

LZMA Utils is a format that uses the LZMA algorithm.

```python
import lzma
lzma.decompress(data, format=lzma.FORMAT_RAW)

# 'Hello World!'
```

## Streaming

LZMA files can be streamed.

```python
import lzma

with lzma.open(filename, "
