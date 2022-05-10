import types
types.FunctionType

# 判断是否是某个类型
def fn():
    pass

isinstance(fn, types.FunctionType)

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
dir('abc')

# len()函数实际上是在做一次dir()，然后做一个判断，看对象里面有没有一个叫__len
