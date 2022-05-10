from types import FunctionType
a = (x for x in [1])
b = (y for y in [2])

def c(x,y):
	return x+y

a = c(a,b)

for i in a:
	print i

def f(x):
	return x+2

g = lambda x : x+1

print f(3)
print g(3)

print isinstance(f,FunctionType)
print isinstance(g,FunctionType)

print type(f)
print type(g)


t = (1,2)
t2 = t,(3,4)
t3 = t2,(5,6)
t4 = t3,(7,8)
t5 = t4,(9,10)
t6 = t5,(11,12)
t7 = t6,(13,14)
t8 = t7,(15,16)
t9 = t8,(17,18)
t10 = t9,(19,20)
t11 = t10,(21,22)

print t11
print type(t
