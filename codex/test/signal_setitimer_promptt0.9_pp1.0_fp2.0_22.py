import signal
# Test signal.setitimer support.
if hasattr(signal, 'setitimer'):
    signal.setitimer(signal.ITIMER_PROF, 1, 0.0001)
    signal.signal(signal.SIGPROF, lambda n,f:1)

# Check whether we can use a private dict instead of a global dict.
from types import FunctionType, ClassType
class X(object):
    pass

def test_private():
    py.test.skip("privates dict not public in python 2.6")
    f = FunctionType((lambda:1).func_code, X.__dict__, "hidden_func")
    c = ClassType("hidden_class", (object,), X.__dict__)
    def f():
        return 1
    c2 = type("hidden_class2", (object,), X.__dict__)
    # print f, f.func_dict, c, c.__dict__
    return f, c, c2


import sys

class Cpu:
    filename = '/proc/stat'
