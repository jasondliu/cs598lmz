import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b"Hello")

// 没有更多的数据可以解压，将会抛出 EOFError。
decompressor.decompress(b"World!")
// 每次任何数据解压之前，首先必须创建一个新的 LZMADecompressor。
decompressor.decompress(b"Hello")

// LZMADecompressor 还可以被用于流式解压 - 即，输入可以分块解压。
decompressor = lzma.LZMADecompressor()

decompressor.decompress(b"foo")
decompressor.decompress
