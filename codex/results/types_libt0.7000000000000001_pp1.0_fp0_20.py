import types
types.ClassType

print type(None)
print type(True)
print type(1)
print type(1.1)
print type('abc')
print type([])
print type(())
print type({})
print type(type(1))
print type(abs)


#使用type()函数判断的基本类型都可以用isinstance()函数判断
print isinstance(123,int)
