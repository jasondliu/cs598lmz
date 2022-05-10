from types import FunctionType
a = (x for x in [1])
print(type(a))

b = lambda x:x
print(type(b))
print(isinstance(b,FunctionType))

print(type(abs))
print(type(str))

print(type(123))
print(type('str'))
print(type(None))

print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print(dir('ABC'))

print('ABC'.__len__())
print('ABC'.lower())

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
print(len(dog))

print('ABC'.lower())

print(hasattr(dog,'x'))
setattr(dog,'x',123)
print(hasattr(dog,'x'))
print(getattr(dog,'x'))

print(getattr(dog,'y',404))

fn =
