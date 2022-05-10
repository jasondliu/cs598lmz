from types import FunctionType
a = (x for x in [1])
print(type(a))
def fun():
    pass
print(type(fun))
print(type(int))
print((type(lambda x: x+1) is FunctionType))  # python2 替换成types.LambdaType
