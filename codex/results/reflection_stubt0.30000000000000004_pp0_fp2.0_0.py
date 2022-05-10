fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'
fn.__dict__ = {'a': 1}
fn.__defaults__ = (1, 2, 3)
fn.__closure__ = (c1, c2)
fn.__globals__ = {'a': 1}
fn.__annotations__ = {'a': 1}
fn.__kwdefaults__ = {'a': 1}

# class
class C:
    pass

# method
class C:
    def m(self):
        pass

# staticmethod
class C:
    @staticmethod
    def sm():
        pass

# classmethod
class C:
    @classmethod
    def cm(cls):
        pass

# property
class C:
    @property
    def p(self):
        pass

# module
import sys

# frame
def f():
    sys._getframe()

# traceback
def f():
    try:
        1/0
    except:

