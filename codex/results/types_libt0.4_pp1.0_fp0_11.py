import types
types.MethodType(f, None, class_name)

# 实例方法绑定到类
def fn(self, name='world'):
    print('Hello, %s.' % name)

class_name = class_name()
class_name.fn = types.MethodType(fn, class_name)
class_name.fn()

# 给实例绑定一个属性
class_name.name = 'Michael'
print(class_name.name)

# 给实例绑定一个方法
def set_age(self, age):
    self.age = age

class_name.set_age = types.MethodType(set_age, class_name)
class_name.set_age(25)
print(class_name.age)

# 给一个实例绑定的方法，对另一个实例是
