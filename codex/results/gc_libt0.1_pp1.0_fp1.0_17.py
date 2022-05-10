import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print(d['primary'])
del a
gc.collect()
print(d['primary'])

# 10
# 10

# 弱引用字典的一个主要用途是实现缓存。
# 如果你有一个计算或者需要大量内存的函数，
# 可以使用一个缓存来提升性能。
# 下面是一个简单的例子：

import urllib.request
import weakref

class WebPage:

