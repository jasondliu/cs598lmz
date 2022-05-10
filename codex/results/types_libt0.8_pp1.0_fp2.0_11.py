import types
types.MethodType(func, obj)

# 实例方法由于第一个参数是self，因此，把原来的类的方法改写成第一个参数是self的方法
# 然后，把方法转换为实例方法
def set_age(self, age):
    self.age = age

s.set_age = types.MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(30)
s.age


# 给类绑定方法,当我们在定义类的时候，可以用__slots__限制实例的属性
class Student
