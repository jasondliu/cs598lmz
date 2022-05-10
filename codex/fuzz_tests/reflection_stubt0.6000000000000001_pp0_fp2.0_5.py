fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
 
#4.
fn = lambda: None
fn.__code__ = type(lambda: 0)
fn()
 
#5.
fn = lambda: None
fn.__code__ = type(lambda: 0).__new__(type(lambda: 0))
fn()
 
#6.
class A(Exception):
    def __init__(self):
        self.__class__ = type('A', (Exception,), {'__init__': lambda self: None})
 
raise A
 
#7.
def fn(self):
    self.__class__ = type('A', (Exception,), {'__init__': lambda self: None})
 
type('A', (Exception,), {'__init__': fn})().with_traceback(None)
 
#8.
type('A', (Exception,), {'__init__': lambda self: None})().with_traceback(None)
 
#9.
type('A', (Exception,), {'__init__': lambda self: None
