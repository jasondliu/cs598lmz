from types import FunctionType
a = (x for x in [1])
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

# 注意：generator 和函数的执行流程不一样。函数是顺序执行，遇到 return 语句或者最后一行函数语句就返回。
# 而变成 generator 的函数，在每次调用 next() 的时候执行，遇到 yield 语句返回，再次执行时从上次返回的 yield 语句处继续执行。
# 举个简单的例子，定义一个包含 yield 的函
