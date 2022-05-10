from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# 不要把实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

hasattr(obj, 'x') # 有属性'x'吗？

setattr(obj, 'y', 19) # 设置一个属性'
