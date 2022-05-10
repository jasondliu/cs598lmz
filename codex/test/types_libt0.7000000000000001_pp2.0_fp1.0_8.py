import types
types.ModuleType

def method(self,x):
	return x+1
method(1)

obj=types.ModuleType('example')
obj.method=method
print(obj.method(1))

import sys

print(sys.getrefcount(obj))
del obj
print(sys.getrefcount(obj))
