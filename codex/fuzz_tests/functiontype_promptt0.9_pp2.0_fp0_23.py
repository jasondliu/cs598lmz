import types
# Test types.FunctionType
'''
我们来判断对象是否是函数
'''
print(type(abs)==types.BuiltinFunctionType)

print(type(lambda x:x)==types.LambdaType)

print(type(x for x in range(10))==types.GeneratorType)

'''
判断class是否是某个其他class的子类
'''
print(isinstance([1,2,3],(list,tuple)))
# getattr()、setattr()以及hasattr(),对对象属性进行操作
class MyObject(object):
	def __init__(self):
		self.x=9

	def power(self):
		return self.x*self.x
obj=MyObject()
print(hasattr(obj,'x'))
print(getattr(obj,'x'))
print(getattr(obj,'y',404))
set
