gi = (i for i in ())
# Test gi.gi_code with a function defined in Python
def gen():
    yield
gi = gen()
def gi_code(gi):
    return gi.gi_code
def gi_frame(gi):
    return gi.gi_frame
def gi_frame_set(gi, new_frame):
    gi.gi_frame = new_frame

# Test gi.gi_frame with a function defined in Python
def gen_frame():
    yield
gi_frame = gen_frame()

import _testcapimodule

class M(object):
    def __init__(self, x):
        self.x = x

def f1(x):
    return M(x)

def f2(x, y):
    return M(x+y)

# Test the descriptor protocol with a function defined in Python
def func():
    pass

class descr(object):
    def __get__(self, obj, type=None):
        return obj

func.attr = descr()

# Test the weakref protocol with a function defined in Python
def
