import types
# Test types.FunctionType and types.MethodType.
# This is a bit tricky, because we need to make sure that the
# types.FunctionType object is actually a function.
# We do this by calling it and making sure it returns the right value.
#
# Also, we need to make sure that the types.MethodType object is
# actually a method of a class, so we check the class of the object.
#

def f():
    pass

class C:
    def m(self):
        pass

print types.FunctionType(f.func_code, f.func_globals)()
print types.MethodType(C.m.im_func, None, C)()

# Test types.ClassType
#
# We need to make sure that the types.ClassType object is actually
# a class, so we check the class of the object.
#

class C:
    pass

print types.ClassType("C", (C,), {}).__class__

# Test types.InstanceType
#
# We need to make sure that the types.InstanceType object is actually
# an instance
