import types
types.ClassType
types.TypeType

import inspect, types
def isclass(object):
    return isinstance(object, (types.ClassType, types.TypeType))

print isclass(1)
print isclass(int)
print isclass(type([]))
print isclass(type(object))
print isclass([])
print isclass(type(isclass))

# Function overloading
def bed(a,b):
    print("a=%s b=%s" % (a,b))

def bed(a):
    print("I was not expecting %s" % (a))

bed("hi","hi")

def bed(a,b):
    print("I am the right one %s" % (a))

bed("hi","hi")

# class overloading
class Foo:
    def __init__(self, x = 0):
        print("x = %s" % (x))

def trace(f, *args):
    print("calling %s (%s)" % (f.__name__, ", ".join(map(str
