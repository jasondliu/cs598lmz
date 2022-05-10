fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_frame = lambda: None
gi.gi_frame.f_globals = {'sys': sys}
# we want to raise the exception in the caller frame
getattr(gi.gi_frame.f_globals['sys'], 'foo', None)
 
class A:
    prop = 42
    def __init__(self, value):
        self.value = value
    def __getattribute__(self, name):
        # disable custom attribute access
        return self.value
 
a = A('foo')
bool.__class__.__base__(a)
 
def f():
    pass
f.__code__.co_firstlineno
 
obj = object()
obj.__class__ = bool
# set __init__ incorrectly, object.__init__ should be called
bool.__base__
 
# must return nonzero
int(True)
 
def bool():
    pass
bool(True)
 
super(int, 42)
 
# check if @classmethods are recognized
class A:
   
