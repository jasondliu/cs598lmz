import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 注意，虽然BZIP2压缩算法很棒，但是它的压缩速度很慢，在很多时候并不能提供足够的性能。
# 如果你需要更快速的压缩，可以使用zlib或gzip模块。
# 如果你需要更高的压缩比，可以使用lzma或bz2模块。
# 如果你需要既要高压缩比又要高性能
