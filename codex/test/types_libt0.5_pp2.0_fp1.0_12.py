import types
types.MethodType(f,None,type)

#给一个实例绑定的方法，对另一个实例是不起作用的
class Student(object):
	pass
s=Student()
def set_age(self,age):
	self.age=age
s.set_age=types.MethodType(set_age,s)
