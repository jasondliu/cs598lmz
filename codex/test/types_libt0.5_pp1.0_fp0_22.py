import types
types.MethodType(my_decorator, None, cls)

# 实际上,上面的方法相当于:
cls.method_with_decorator = my_decorator(cls.method_with_decorator)
