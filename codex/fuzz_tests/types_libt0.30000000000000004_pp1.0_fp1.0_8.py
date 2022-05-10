import types
types.MethodType(func, None, class_name)

# 要给所有实例都绑定方法，可以给class绑定方法：
class_name.func = func
class_name.func()

# 通常情况下，上面的set_age方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
