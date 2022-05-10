import types
# Test types.FunctionType
def f():
    pass

class C(object):
    def meth(self):
        pass

print type(f) is types.FunctionType  # True
print type(C.meth) is types.FunctionType  # True

import types
# Test type.MethodType
def f(self):
    f.called = True

f.called = False
class C(object): pass
C.meth = types.MethodType(f, C())
C.meth()

print f.called  # True

print C.__dict__  # {'meth': <function __main__.f>, '__module__': '__main__'}

import types
# Test type.MethodType
def f(self):
   f.called = True

f.called = False
class C(object): pass
C.meth = types.MethodType(f, None, C)
C().meth()

print f.called  # True

print C.__dict__  # {'meth': <function __main__.f>, '__module__
