import types
types.MethodType

# 我们也可以给类加上方法
def set_age(self,age):
    self.age = age

def set_score(self,score):
    self.score = score

# 给类加上方法
Student.set_age = set_age
Student.set_score = set_score

s.set_age(25)
s.set_score(100)
print(s.age)
print(s.score)


# 使用__slots__限制类成员变量
# __slots__的限定只对当前类的实例起作用，对继承的子类是不起作用的
class Teacher(object):
    __slots__ = ("name", "age")

t = Teacher()
t.name = "qiu"
t.age
