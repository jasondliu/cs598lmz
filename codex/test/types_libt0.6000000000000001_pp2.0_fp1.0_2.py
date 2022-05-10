import types
types.MethodType

# 给别的类的实例绑定方法，也可以
# 只是，此时，只能在实例上调用，而不能在类上调用
class Student2(object):
    pass
s2 = Student2()
def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age
s2.set_age = types.MethodType(set_age, s2) # 给实例绑定一个方法
s2.set_age(25) # 调用实例方法
s2.age # 测试结果

# 但是，给一个实例绑定的
