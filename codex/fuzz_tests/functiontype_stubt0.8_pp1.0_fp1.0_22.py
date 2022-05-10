from types import FunctionType
a = (x for x in [1])
print isinstance(a, GeneratorType)


# 获取对象信息
def fn():
    pass


a = fn
print type(a)
print type(fn)
print type(222)
print type({})
print type([])
#
#
# print dir(a)
#
#
# print hasattr(a, '__len__')
#
#
# attr = getattr(a, '__len__')
# print attr
# print attr()
# print callable(attr)
# print type(attr)
# print callable(a)
# print type(a)
#
#
# print hasattr(a, 'name')
# print type(getattr(a, 'name'))
#
#
# setattr(a, 'name', 'aaa')
# print getattr(a, 'name')
#
# print getattr(a, '__len__')()
#
# print setattr(a, '__len__', lambda: 200)
# print getattr(a
