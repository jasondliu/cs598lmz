import types
types.MethodType(func, None, class_name)

class_name.func()

# 给实例绑定方法
def func(self):
    print('实例方法')

class_name.func = types.MethodType(func, class_name)

class_name.func()

# 给实例绑定方法
def func(self):
    print('实例方法')

class_name.func = types.MethodType(func, class_name)

class_name.func()

# 给实例绑定方法
def func(self):
    print('实例方法')

class_name.func = types.MethodType(func, class_name)

class_name.func()

# 给实例绑定方法
def func(self):
    print('实例方法')

