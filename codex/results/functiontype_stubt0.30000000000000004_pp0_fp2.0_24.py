from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = {1,2,3}
d = {1:1,2:2}
e = 1
f = '1'
g = FunctionType
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

# 判断是否为某种类型
print(isinstance(a,GeneratorType))
print(isinstance(b,list))
print(isinstance(c,set))
print(isinstance(d,dict))
print(isinstance(e,int))
print(isinstance(f,str))
print(isinstance(g,FunctionType))

# 判断是否为某种类型
print(isinstance(a,(GeneratorType,list)))
print(isinstance(b,(GeneratorType,list)))
print(isinstance(
