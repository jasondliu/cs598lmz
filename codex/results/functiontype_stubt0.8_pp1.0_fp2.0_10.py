from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = dict(a=1)
def d():
    pass

e = True
f = 1
g = 1.5
h = 'a'

print('a type is',type(a))
print('b type is',type(b))
print('c type is',type(c))
print('d type is',type(d))
print('e type is',type(e))
print('f type is',type(f))
print('g type is',type(g))
print('h type is',type(h))

print('type is',isinstance(b, list))
print('type is',isinstance(b, type(a)))
print('type is',isinstance(d, FunctionType))

'''
判断对象类型，使用type()和isinstance()函数。
相较于type()，isinstance()自动判断一个变量类
