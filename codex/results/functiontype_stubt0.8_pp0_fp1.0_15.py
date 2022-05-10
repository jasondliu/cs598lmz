from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(iter))
print(type(iter([1])))
print(type(next))
print(type(FunctionType))


print('')
print('----class')
class ITest:
    pass

a = ITest()
print(type(a))
print(type(a.__class__))
print(type(ITest))
