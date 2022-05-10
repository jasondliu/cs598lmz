import types
types.ClassType

#获取对象信息
#使用type()
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

print(type(123)==type(456))
print(type(123)==int)
print(type('abc')==type('123'))
print(type('abc')==str)
print(type('abc')==type(123))

#使用isinstance()
print(isinstance('a',str))
print(isinstance(123,int))
print(isinstance(b'a',bytes))

#能用type()判断的基本类型也可以用isinstance()判断
print(isinstance([1,2,3],(list,tuple)))
print(isinstance((1,2,3),(list,tuple)))

#使用dir()
#如果要获得一
