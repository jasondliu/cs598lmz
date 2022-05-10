from lzma import LZMADecompressor
LZMADecompressor().decompress(response.content)

# 可以看到，使用多进程爬虫没有加快速度，反而变慢了，这是因为
# 网站对于同一个IP地址的访问有频率限制，而且我们在多进程爬虫中，
# 每个进程都有自己的IP地址，即便有一个进程被限制，也有其他进程
# 可以继续访问，这样爬虫会更快
