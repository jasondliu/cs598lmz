from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# 使用 bz2 模块
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)

# 使用 zlib 模块
import zlib
zlib.decompress(compressed)

# 使用 gzip 模块
import gzip
with gzip.GzipFile(fileobj=compressed) as f:
    f.read()

# 在响应中自动解压缩
import requests
r = requests.get('https://www.python.org/')
r.headers['Content-Encoding']
r.text

# 处理压缩的文件
import gzip
import shutil
with gzip.open('somefile.gz', 'rb') as f_in:
    with open('somefile.txt', 'wb') as f_out:
        shutil.copyfileobj(f_
