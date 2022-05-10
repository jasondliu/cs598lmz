from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

import bz2
bz2.decompress(data)

import lz4.frame
lz4.frame.decompress(data)

import lzma
lzma.decompress(data)

import zstandard
zstd.ZstdDecompressor().decompress(data)

import zlib
zlib.decompress(data)

import brotli
brotli.decompress(data)

import snappy
snappy.decompress(data)
```

## Compression and decompression using cbor2 and cbor

```python
import cbor2
cbor2.loads(data)

import cbor
cbor.loads(data)
```

## Compression and decompression using msgpack

```python
import msgpack
msgpack.unpackb(data, raw=False)
```

## Compression and decompression using ujson

```python
import ujson
ujson.loads(data)
```

## Compression
