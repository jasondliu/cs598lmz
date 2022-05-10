import types
types.MethodType(myFunc,obj)
obj.myFunc()

#设置属性
obj.name='new name'
obj.name

#给实例绑定一个方法
def set_age(self,age):
	self.age=age

from types import MethodType

obj.set_age=MethodType(set_age,obj)
obj.set_age(19)
obj.age

#给一个实例绑定方法，对另一个实例不起作用
obj2=Student()
obj2.set_age(18)

#给一个类绑定方法
def set_score(self,score):
	self.score=score

Student.set_score=set_score
obj.set_score(100)
obj.score
obj2.set_score(99)
obj2.score

