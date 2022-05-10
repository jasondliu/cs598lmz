import types
# Test types.FunctionType, types.MethodType and types.LambdaType
# objects, introduced in Python 2.2

import types

def f(x):
    return x

class C(object):
    def f(self, x):
        return x

c = C()

print(types.FunctionType, types.MethodType, types.LambdaType)
print(type(f), type(c.f))
print(isinstance(f, types.FunctionType), isinstance(c.f, types.MethodType))

# Test types.ClassType, and types.InstanceType objects, removed in
# Python 3

# class D(object):
#     pass
#
# d = D()
#
# print(types.ClassType, types.InstanceType)
# print(type(D), type(d))
# print(isinstance(D, types.ClassType), isinstance(d, types.InstanceType))
