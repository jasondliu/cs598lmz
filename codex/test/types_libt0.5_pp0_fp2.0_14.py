import types
types.MethodType(func, obj)

# 给实例绑定属性
obj.name = 'aaa'

# 给实例绑定方法
def func(self):
    print('hello')
obj.func = types.MethodType(func, obj)
obj.func()

# 给类绑定方法
def func(self):
    print('hello')
