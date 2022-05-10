import ctypes
ctypes.cast(0, ctypes.py_object).value

# 创建一个空的类
class EmptyClass:
    pass

# 创建一个有属性的类
class Person:
    name = 'Person'

# 创建一个实例
somebody = Person()

# 访问类的属性
somebody.name

# 修改类的属性
somebody.name = 'Mr. Gumby'

# 删除类的属性
del somebody.name

# 创建一个有方法的类
class Person:
    def say_hi(self):
        print('Hello, how are you?')

# 创建一个实例
p = Person()

# 调用类的方法
p.say
