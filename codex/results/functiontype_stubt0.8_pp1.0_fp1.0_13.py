from types import FunctionType
a = (x for x in [1])
b = {x for x in [1,2]}
c = [1]

print(isinstance(a,GeneratorType))
print(isinstance(b,Set))
print(isinstance(c,List))
print(isinstance(abs,FunctionType))

# 实例属性和类属性：
class Student(object):
    name='Student'   #类属性
s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)

# 使用@property
class Student(object):
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value >100:
            raise ValueError('score must between 0~100!
