from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 可以使用一个类来表示一个不需要初始化的简单函数对象，比如，下面的代码创建了一个接受一个或多个数并计算乘积的类
class Product:
    def __init__(self):
        self.current = 1

    def __call__(self, value):
        self.current *= value
        return self

product = Product()
print(product(2)(3)(4))

# 实现一个简单的通用的日志系统，可以记录日志到文件和终端
import logging
logging.basic
