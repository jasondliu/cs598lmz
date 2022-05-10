import types
types.MethodType(f, None, Student)
Student.speak = f
s = Student()
s.speak()
s2 = Student()
s2.speak()

# __slots__
class GraduateStudent(Student):  #子类中定义的__slots__不会对父类及其实例造成影响
    pass
g = GraduateStudent()
g.name = 'Michael'
g.age = 25
print(g.score)
g.score = 9999
print(g.score)

class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'

