import types
types.MethodType(lambda self: None, None, object)

# TypeError: unbound method <lambda>() must be called with object instance as first argument (got nothing instead)

# 上面的代码中，我们自定义了一个函数lambda x: x * x，并且把它赋值给一个变量f，
# 这个变量f现在已经不仅仅是函数，而是一个可以记住状态的函数，并且可以像普通函数一样进行调用f(5)。

# 还记得装饰器（decorator）可以给函数动
