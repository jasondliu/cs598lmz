import types
types.MethodType(func, obj)

# 可以给一个实例绑定一个方法，该实例可以调用这个方法

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的

# 为了给所有实例都绑定方法，可以给class绑定方法
# 给class绑定方法后，所有实例均可调用

def set_age(self, age):
    self.age = age

Student.set_age = set_age

s.set_age(25)
s.age

s2.set_age
