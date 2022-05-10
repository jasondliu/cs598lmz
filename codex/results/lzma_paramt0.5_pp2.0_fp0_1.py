from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# %%
# 这个解压缩器支持非阻塞的流式解压缩。 为了使用它，你需要创建一个解压缩器对象，然后
# 不断的调用它的 decompress() 方法来解压缩数据。 当你没有更多的数据块可以输入时，你需要调
# 用 flush() 方法来获取解压缩后剩余的数据。

# 通常情况下，解
