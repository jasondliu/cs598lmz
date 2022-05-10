import types
types.MethodType(f, None, Student)

# 测试:
s = Student()
s.name = 'Michael'
s.score = 99
print(s.name)
print(s.score)
s.print_score()

s.set_age(25)
print(s.get_age())
print(s.age())

# 给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student()
# s2.set_age(25) #报错AttributeError: 'Student' object has no attribute 'set_age'


# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score

Student.set_score = set_score


