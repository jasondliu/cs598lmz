from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(data)) == data
```

```
True
```

### `gzip`

```python
import gzip
gzip.decompress(gzip.compress(data)) == data
```

```
True
```

`gzip`是最常用的压缩格式，这既是因为它拥有较好的压缩率，在客户端和服务端之间也具有很好的支持。比如在HTTP头中使用`Content-Encoding`标识数据是通过`gzip`压缩过的。

#### gzip 压缩/解压缩示例

```python
import gzip

with g
