import types
types.MethodType(f, None, None)

class Student(object):
    pass
s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
