import weakref
# Test weakref.ref further - specifically check that callbacks etc work.

class Foo(object):
    def __init__(self, name):
        self.name = name

def callback(wr, arg):
    global BEGGED
    BEGGED = arg

def callback_tuple(wr, (arg1, arg2)):
    global BEGGED
    BEGGED = (arg1, arg2)

alive = weakref.liveref(Foo("alive"))
BEGGED = None
del alive
assert BEGGED is None

alive = weakref.liveref(Foo("alive"))
BEGGED = None
del alive()
assert BEGGED == "alive"

alive = weakref.liveref(Foo("alive"))
BEGGED = None
arg = 1
weakref.add_callback(alive, callback, arg)
del alive()
assert BEGGED == arg

alive = weakref.liveref(Foo("alive"))
BEGGED = None
arg = 1
