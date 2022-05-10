import types
types.MethodType(f, None, Student)
# 运行方法
# 可以在实例上直接调用定义的方法，在形参里面传入self
s.run()
# 可以在类上调用方法，在形参里面传入实例
Student.run(s)
# 实例属性和类属性
# 实例属性属于实例的，类属性相当于类的公共属性
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1
