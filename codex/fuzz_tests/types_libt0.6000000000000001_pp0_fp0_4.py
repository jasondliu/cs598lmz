import types
types.MethodType(f,None,type)

# 定制类
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'

bart=Student('Bart Simpson',59)
lisa=Student('Lisa simpson',87)
bart.print_score()
lisa.print_score()
print(bart.get_grade())
print(lisa.get_grade())

# 修改类
bart.age=8
print(bart.age)

# 修改实例的属性
bart.score=99
print(bart.score)

# 
