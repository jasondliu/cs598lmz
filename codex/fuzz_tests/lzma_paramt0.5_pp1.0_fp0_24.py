from lzma import LZMADecompressor
LZMADecompressor().decompress(x)

# 还有一个与 zlib 类似的压缩格式，叫 bz2。它的压缩算法比 zlib 更复杂，所以通常效率更高，
# 但是同时也更慢。
import bz2
bz2.compress(x)
bz2.decompress(x)

# 如果你不想自己去操心压缩算法的复杂性，那么可以使用一个简单的封装层来处理这些细节。
# 例如，可以使用 gzip 或 bz2
