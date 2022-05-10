from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a==b)
print(a is b)
print()

print('a is __iter__',b.__iter__ is a.__iter__)
print()

#print('show func_closure',b.func_closure is a.func_closure)
print()

print('a is function',FunctionType is type(a))
print()
def a():
    pass

def b():
    pass

#print('a is function',type(a) is type(b))
print('a is function',type(a) == type(b))
print()
