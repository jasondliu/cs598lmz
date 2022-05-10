import types
types.MethodType(f,None,Student)

#给实例绑定属性
s.name='Michael'
#给实例绑定方法
s.print_score=MethodType(f,s)
s.print_score()

#给class绑定方法
Student.print_score=f
s.print_score()

#限制实例属性
class Student(object):
    __slots__=('name','age')
s=Student()
s.name='Michael'
s.age=25
#s.score=99

#使用@property
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('
