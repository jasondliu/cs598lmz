import types
# Test types.FunctionType()
def func(x):
  return x
 
print(type(func), type(func()) )
print(type(func), type(func(2)) )
print(type(func), type(func(x=2)) )

print(type(func), type(func(x=3, y=4)) )

print(func.__call__(2))
print(func.__call__(x=2))

print(type(func.__call__) )

#print(func.__call__(x=3, y=4))

#print(func.__call__())

#print(func(x=2))
#print(func(x=3, y=4))
#print(func())

#x = 4
#print(func(x))

y = 5
print(func(y))

#print(func(2*y))

#print(func())

print(type(func) )
print(func.__call__)

print(type(func.__call__) )

#print(
