from types import FunctionType
a = (x for x in [1])
print(type(a))
b = lambda x:x
print(type(b))
print(type(abs))
print(type(FunctionType))
print(type(None))
print(type(123))
print(type('s'))
print(type(1.1))
print(type(abs))
def f():
    pass
print(type(f) == types.FunctionType)
print(type(f) == types.LambdaType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)
#使用isinstance()
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))
print(isinstance(None,str))
#使用dir()
print(dir('ABC'))
print(len
