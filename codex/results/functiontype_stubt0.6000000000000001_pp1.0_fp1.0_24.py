from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a==b)
print(type(a))
print(isinstance(a,FunctionType))

print(dir(a))
print(a.__closure__)
print(a.__closure__[0])
print(a.__closure__[0].cell_contents)
print(a.__code__.co_varnames)
print(a.__code__.co_argcount)

#经过分析，可以看到generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，
