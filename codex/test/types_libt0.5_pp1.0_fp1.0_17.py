import types
types.MethodType(f,None,class_name)
#给实例绑定一个方法
def set_age(self,age):
    self.age=age

from types import MethodType
class_name.set_age=MethodType(set_age,class_name)
class_name.set_age(25)
class_name.age
#给一个实例绑定的方法，对另一个实例是不起作用的
class_name2=Student('lisi')
class_name2.set_age(24)

#为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score=score
Student.set_score=set_score
class_name.set_score(100)
class_name.score
