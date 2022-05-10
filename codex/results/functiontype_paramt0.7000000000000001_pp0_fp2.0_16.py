from types import FunctionType
list(FunctionType(lambda x:x*x,{},'__call__') for x in range(4))

from types import MethodType
foo = MethodType(lambda x:x*x,None,'foo')
foo(4)

from types import ModuleType
foo = ModuleType('foo','')
foo.__name__

from types import GeneratorType
def foo():
    yield 1
    yield 2
foo()
list(foo())
type(foo())
list(foo())

from types import CodeType, TracebackType
import dis
foo = lambda x:x*x
dis.dis(foo)
foo.__code__

import inspect
inspect.getmembers(foo.__code__)

import sys
list(TracebackType(sys.last_traceback).tb_frame.f_code)

import __builtin__
__builtin__.__import__('math')

import sys

import types
from types import FrameType, TracebackType

class _Helper:
    def __init__(self):
        pass
    def __call__(self):
