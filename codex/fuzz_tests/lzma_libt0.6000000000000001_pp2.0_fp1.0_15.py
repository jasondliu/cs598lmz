import lzma
lzma.LZMADecompressor.decompress

# 编码器
lzma.LZMACompressor()

# 解码器
lzma.LZMADecompressor()

# 读取
lzma.open(filename)

# 解压
lzma.decompress(data)

# 压缩
lzma.compress(data)

# 压缩文件
lzma.compressfile(fileobj)

# 解压文件
lzma.decompressfile(fileobj)

# 支持的压缩算法
lzma.FORMATS

# 支持的模式
lzma.MODES
```

### `json`

```py
import json

# 序列化
json.dumps(obj)

# 反
