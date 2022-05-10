from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 使用LZMA压缩数据
import lzma
LZMA_PATH = '/tmp/file.xz'
with lzma.open(LZMAD_PATH, 'wb') as f:
    f.write(b'Hello World')
# 读取
with lzma.open(LZMA_PATH) as f:
    print(f.read())
