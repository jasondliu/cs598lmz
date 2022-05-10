import types
# Test types.FunctionType and types.LambdaType
def test():
    print("test")

if type(test) is types.FunctionType:
    print("test is a function")
else:
    print("test is not a function")

if type(lambda x: x) is types.FunctionType:
    print("lambda is a function")
else:
    print("lambda is not a function")

class C:
    def aMethod(self):
        print("aMethod")

if type(C) is types.FunctionType:
    print("C is a function")
else:
    print("C is not a function")

if type(C.aMethod) is types.FunctionType:
    print("C.aMethod is a function")
else:
    print("C.aMethod is not a function")

# import sys
# print(sys.version)
#
# from test import *
# a = A()
# print(a.a_func())
#
# print(type(a))
