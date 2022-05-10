import types
# Test types.FunctionType
def f(): pass
def g(): pass
f.__dict__['x'] = 42
f.__dict__['y'] = 42
g.__dict__['x'] = 42
g.__dict__['y'] = 43
f.__dict__['z'] = 42
f.__dict__['zz'] = 42
f.__dict__['zzz'] = 42
def mycmp(x, y):
    return cmp(x.__dict__, y.__dict__)
functions = [f, g]
functions.sort(mycmp)
print functions[0] is g
print functions[1] is f
# Test types.InstanceType
class A:
    def __init__(self):
        self.x = 42
        self.y = 42
        self.z = 42
        self.zz = 42
        self.zzz = 42
class B(A):
    def __init__(self):
        A.__init__(self)
        self.y = 43
instances = [A(), B()]
instances.sort(mycmp
