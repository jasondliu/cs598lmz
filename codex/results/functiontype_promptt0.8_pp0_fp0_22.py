import types
# Test types.FunctionType, types.MethodType, types.BuiltinMethodType and types.LambdaType.
# Should not crash.

class MyObject():
    def method1(self):
        print 1

    def method2(self):
        print 2

def func1():
    print 1

def func2():
    print 2

def func3():
    print 3

def test1(obj):
    if isinstance(obj, types.MethodType):
        method = obj.im_func
    else:
        method = obj

    if isinstance(method, types.FunctionType):
        return method

def test2(obj):
    if isinstance(obj, types.MethodType):
        method = obj.im_func
    else:
        method = obj

    if isinstance(method, types.FunctionType):
        return method

    if isinstance(method, types.LambdaType):
        return method

def test3(obj):
    if isinstance(obj, types.MethodType):
        method = obj.im_func
    else:
        method =
