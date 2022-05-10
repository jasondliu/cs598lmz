import types
types.MethodType(lambda self, x: x, None, object)

# TypeError: unbound method must be called with instance as first argument (got nothing instead)

# MethodType(func, instance, class)

# func: 方法的实现函数
# instance: 方法的绑定对象
# class: 方法的绑定类

# 这个方法的作用是给一个对象绑定一个方法，使用这个方法可以给任意对象绑定方法，但是只能绑定在对象上，不能绑定在类上。

# 下面的例子给一个对象绑定一个
