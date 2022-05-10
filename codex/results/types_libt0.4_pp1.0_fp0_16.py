import types
types.MethodType(f, None, Student)

# 给实例绑定一个方法
s.print_score = types.MethodType(f, s)
s.print_score()

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student('bob', 99)
# s2.print_score()

# 给class绑定方法后，所有实例均可调用
def set_age(self, age):
    self.age = age

Student.set_age = set_age

s.set_age(25)
s.age

s2.set_age(26)
s2.age

# 使用__slots__
# 但是，如果我们
