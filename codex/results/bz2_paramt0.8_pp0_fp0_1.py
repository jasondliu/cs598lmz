from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(response.body)

# 另一个例子是使用gzip或者deflate压缩，这种压缩在HTTP响应中有一个Content-Encoding头来指示
import gzip
from io import BytesIO
gzip_compress = gzip.GzipFile(fileobj=BytesIO(response.body))
gzip_compress.read()

# 压缩后的数据还原
import zlib
zlib.decompress(response.body)

# Scrapy会自动为我们处理网页数据的压缩。
# 如果某些网站没有正确地声明压缩方式，可以使用下
