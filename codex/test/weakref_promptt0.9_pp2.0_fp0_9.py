import weakref
# Test weakref.ref further - specifically check that callbacks etc work.

class Foo(object):
    def __init__(self, name):
        self.name = name

def callback(wr, arg):
    global BEGGED
    BEGGED = arg

