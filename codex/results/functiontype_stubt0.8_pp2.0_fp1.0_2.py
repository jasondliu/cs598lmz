from types import FunctionType
a = (x for x in [1])
print isinstance(a,FunctionType)


#实例属性和类属性
#由于Python是动态语言，根据类创建的实例可以任意绑定属性
#给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
	def __init__(self,name):
		self.name = name
s = Student('Bob')
s.score = 90 # 动态给实例绑定一个属性
print s.score

#如果Student类本身需要绑定一个属性呢？
