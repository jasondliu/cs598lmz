from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# 如果你想对大块的二进制数据进行压缩，可以使用一个基于内存的压缩数据流。
# 例如，下面是一个将二进制数据压缩到一个内存中的 BytesIO 对象中的例子：
import io
from bz2 import BZ2Compressor
compressor = BZ2Compressor()
f = io.BytesIO()
f.write(compressor.compress(data))
f.write(compressor.flush())
f.getvalue()

# 如果你想在文件上执行压缩，可以使用一个
