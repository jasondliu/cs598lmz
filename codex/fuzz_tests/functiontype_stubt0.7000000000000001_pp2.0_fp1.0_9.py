from types import FunctionType
a = (x for x in [1])
isinstance(a, GeneratorType)

# 判断是否是int
isinstance(1, int)

# 判断是否是str
isinstance("zhangsan", str)

# 判断是否是dict
isinstance({"name": "zhangsan"}, dict)

# 判断是否是list
isinstance([1, 2, 3], list)

# 判断是否是set
isinstance({1, 2, 3}, set)

# 判断是否是tuple
isinstance((1, 2, 3), tuple)

# 判断是否是function
isinstance(print, FunctionType)

# 判断是否是class
class Test(object):
    pass

isinstance(Test(), Test)
