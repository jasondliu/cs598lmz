import types
types.MethodType(foo, obj)

# 允许定义全局函数
def bar():
    pass

# 但不允许给全局函数绑定属性
bar.score = 90

# 允许给类绑定属性
class MyObject(object):
    pass

obj = MyObject()
obj.score = 90

# 但不允许给类绑定函数
def bar():
    pass

MyObject.bar = bar
