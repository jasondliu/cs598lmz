import types
types.MethodType(lambda self, x: x, None, object)

# TypeError: unbound method must be called with instance as first argument (got nothing instead)

# MethodType(func, instance, class)

# func: 方法的实现函数
# instance: 方法的绑定对象
# class: 方法的绑定类

