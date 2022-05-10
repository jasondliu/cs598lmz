import types
types.FunctionType

def f():
    pass

type(f)

isinstance(f, types.FunctionType)

import types
types.BuiltinFunctionType

def f():
    pass

type(f)

import types
types.LambdaType

f = lambda x: x + 1

type(f)

import types
types.GeneratorType

def f():
    yield 1

type(f())

import types
types.CodeType

def f():
    pass

type(f.__code__)

import types
types.TracebackType

try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    type(tb)

import types
types.FrameType

def f():
    pass

type(f.__code__.co_frame)

import types
types.GetSetDescriptorType

class C(object):
    def getx(self): return self.__x
    def setx(self, value): self
