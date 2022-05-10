from types import FunctionType
a = (x for x in [1])
def test():
    print('test')
test.__name__ = 'test'
test.__qualname__ = 'test'
print(isinstance(a, GeneratorType))
print(isinstance(test, FunctionType))
print(isinstance(test, types.FunctionType))
print(type(test))
print(types.FunctionType)
print(types.GeneratorType)
print(types.MethodType)
print(types.TracebackType)
print(type(None))
print(types.NoneType)

# 所谓的面向对象编程，其实就是面向对象的编程思想，即将一个复杂的现实世界中的事物建模成一个个对象，而对象之间可以通过方法来相
