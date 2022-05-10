from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x:x))
print(type(abs))
print(type(a) == types.GeneratorType)
print(type(lambda x:x) == FunctionType)
print(type(abs) == BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type(abs) == types.BuiltinFunctionType)

#使用isinstance()
print(isinstance([1,2,3], (list,tuple)))
print(isinstance((1,2,3), (list,tuple)))
print(isinstance(123, (list,tuple)))

#使用dir()
print(dir('ABC'))
print('ABC'.__len__())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

print('ABC'.lower())
print(len('ABC'))
print('ABC'.__len__())

class MyObject(object):
    def __init
