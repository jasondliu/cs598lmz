import ctypes
ctypes.cast(addr, ctypes.py_object).value

############################################################################
# dict
dict(m=1, n=2)
{'n': 2, 'm': 1} # 键值对不按插入顺序排列
{x:x**2 for x in (2,4,6)}
{k:v for v, k in enumerate("ABC")}

############################################################################
# operator.itemgetter(item), operator.attrgetter(attr)
ipairs = [("ninety", 90), ("sixty", 60), ("ten", 10)]
ipairs.sort(key=operator.itemgetter(1))
ipairs.sort(key=lambda x: x[0])
print ipairs

# call
class Item(object):
    def __init__(self, name, value):
        self._name = name
        self._value = value
    def __repr__(self):
        return "{0}({1}, {2})".format(self.__class__.__name__
