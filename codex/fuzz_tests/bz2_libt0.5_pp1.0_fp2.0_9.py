import bz2
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# 此外还有一种比BZIP2更少见的压缩格式是LZMA，它可以创建比gzip更小的压缩文件，
# 但是它的速度比gzip慢的多，而且需要更多的内存。

# 尽管通常我们会直接使用这些压缩格式
