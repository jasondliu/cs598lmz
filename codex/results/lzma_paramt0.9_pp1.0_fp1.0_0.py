from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00\x04\x00\x00\x00\x00\x00\x01\x00\x00\x00\x1a\x00\x00\x00\x09\x00\x08\x00\x00\x00\x00\x00\x00\t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x10\x00\x03')

# print(Foo.__subclasses__())
# [<class '__main__.Bar'>, <class '__main__.Baz'>]
#
# Bar = Foo.__subclasses__()[0]
# b = Bar()
# b.y = 10
# print(b.__class__)
# __main__.Bar

# pickle.loads(x)
# 就是 (1) 反序
