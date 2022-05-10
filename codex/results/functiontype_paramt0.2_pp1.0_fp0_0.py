from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), 'add_one')(i) for i in range(3))

# [1, 2, 3]

# 使用lambda表达式创建匿名函数时，其实是创建了一个FunctionType类型的对象，并将其作为参数传递给了list函数。
# 在Python中，函数也是对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
# 因为函数也是对象，而且函数对象
