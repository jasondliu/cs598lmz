import types
types.ClassType

# 判断对象类型，使用isinstance()函数。
print isinstance(123, int)
print isinstance('abc', str)
print isinstance(u'abc', unicode)

# 判断一个对象是否是函数
def fn():
    pass
print isinstance(fn, types.FunctionType)
print isinstance(abs, types.BuiltinFunctionType)
print isinstance(lambda x: x, types.LambdaType)
print isinstance((x for x in range(10)), types.GeneratorType)

# 使用dir()
print dir('ABC')

# len()函数
print len('ABC')
print len('中文')

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__
