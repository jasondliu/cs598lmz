import types
types.MethodType(my_decorator, None, cls)

# 实际上,上面的方法相当于:
cls.method_with_decorator = my_decorator(cls.method_with_decorator)

# 这种在运行期动态增加功能的方式,称之为"装饰器"(Decorator)
# 本质上,decorator就是一个返回函数的高阶函数
# 它和高阶函数的区别在于,它会将被装饰的函数作为参数传入


# Python的decorator可以用函数实现,也可以用类实现

