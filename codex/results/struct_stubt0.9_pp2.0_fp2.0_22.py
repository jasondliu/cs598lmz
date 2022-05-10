from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)
print(s.unpack(1))

# 闭包应用
def sample():
    n = 0
    def func():
        print('n = ',n)
    def get_n():
        return n
    def set_n(n1):
        nonlocal n
        n = n1
    func.get_n = get_n
    func.set_n = set_n
    return func

f  = sample()
print(f())
print(f.get_n())
print(f.set_n(10))
print(f())

# generator
# 可迭代对象
from collections import Iterable, Iterator
isinstance([], Iterable)
isinstance([], Iterator)
isinstance((), Iterable)
isinstance((), Iterator)
isinstance('', Iterable)
isinstance('', Iterator)
isinstance(123, Iterable)
isinstance(123, Iterator)

from collections import Iterable
