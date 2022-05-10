import types
types.MethodType(lambda x: x, obj)

# 为了给所有实例都绑定方法，可以给class绑定方法：

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

Student.set_age = set_age

# 通常情况下，上面的set_age方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

# 使用__slots__
