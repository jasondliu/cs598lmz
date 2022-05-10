import ctypes
ctypes.cast(1, ctypes.py_object)

# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
#
# 比方说我们要定义一个Hello的class，就写一个hello.py模块：
#
# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)
# 这就是动态语言最灵活的地方，随时都可以创建出新的类和函数，当然
