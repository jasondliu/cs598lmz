import types
types.MethodType(f, None, class_name)

# 动态给实例绑定一个属性
setattr(instance, 'name', 'Michael')
instance.name

# 动态给类绑定一个属性
setattr(class_name, 'name', 'Michael')
class_name.name

# 动态给实例绑定一个方法
setattr(instance, 'power', lambda x: x * x)
instance.power(2)

# 动态给类绑定一个方法
setattr(class_name, 'power', lambda x: x * x)
class_name.power(2)

# 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student()
