from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print(a == b)
print(a is b)
print(type(a) == type(b))
print(type(a))
print(type(b))
print(FunctionType == type(a))

print(list(a))
print(list(b))

print(eval('1+2'))

print(eval('[1,2,3][0]'))
print(eval('[1,2,3][0+1]'))
print(eval('[1,2,3][1]'))
print(eval('[1,2,3][1+1]'))
print(eval('[1,2,3][2]'))

c = [1,2,3]
print(eval('c[0]'))
print(eval('c[0+1]'))
print(eval('c[1]'))
print(eval('c[1+1]'))
print(eval('c[2]'))

print(eval('1+2'))
print(eval('3+4'))


