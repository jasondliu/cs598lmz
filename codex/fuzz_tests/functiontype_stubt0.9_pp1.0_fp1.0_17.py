from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
a = 12
print(type(a))
print(isinstance(a, int))
print(isinstance(a, (int, float, bool)))

class A:
    pass

class B(A):
    pass

print(isinstance(B(), A))
print(type(B()) == A)

print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)

aa = ['str1', 'str2']
bb = ['str3', 'str4']
print(dir('ABC'))
print(dir(aa))
print(len('ABC'))
print(len(aa))

class MyDog(object):
    def __len__(self):
        retu
