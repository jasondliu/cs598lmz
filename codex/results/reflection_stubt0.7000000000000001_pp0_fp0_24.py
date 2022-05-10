fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.func_code = gi.gi_frame.f_code
fn()
"""

# pure Python code, will not crash
"""
python_code = """
import sys

def foo(cls):
    def __getattribute__(self, name):
        print('accessing', name)
        return cls.__getattribute__(self, name)
    def __setattr__(self, name, value):
        print('setting', name)
        return cls.__setattr__(self, name, value)
    cls.__getattribute__ = __getattribute__
    cls.__setattr__ = __setattr__
    return cls

@foo
class Dummy(object):
    def __init__(self):
        self.x = 1

print('Dummy.x:', Dummy.x)
print('Dummy().x:', Dummy().x)
"""

python_code = """
import sys

def foo(cls):
    def __getattribute__(self, name):
        print('accessing', name)
