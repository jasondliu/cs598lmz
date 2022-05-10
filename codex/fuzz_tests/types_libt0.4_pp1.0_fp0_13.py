import types
types.MethodType

# 定义一个函数作为实例方法
def set_age(self, age):
    self.age = age

# 给实例绑定一个方法
s.set_age = MethodType(set_age, s) # 第一个参数是方法名，第二个参数是实例对象
s.set_age(25)
s.age

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
s2.set_age(25)

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score
