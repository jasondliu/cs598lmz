import ctypes
FUNTYPE = ctypes.CFUNCTYPE(c_int, c_int, c_int)
print(type(FUNTYPE))

# create empty class
print('--- create empty class')
class Empty: pass
print(Empty)
print(dir(Empty))
print('--- create instance')
x = Empty()
print(x)
print(dir(x))
print('--- create instance2')
y = Empty()
print(y)
print(dir(y))

# create object
print('--- create object')
class Object: pass
o = Object()
o.x = 1
o.y = 2
print(o.x, o.y)
o.y = 3
print(o.x, o.y)
del o.x
print(hasattr(o, 'x'), hasattr(o, 'y'))
setattr(o, 'y', 3)
print(hasattr(o, 'z'), hasattr(o, 'y'))
print(getattr(o, 'y', 4), getattr(o, 'z', 4))

# create class
# create class: __init__ function
