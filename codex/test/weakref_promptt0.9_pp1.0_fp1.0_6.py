import weakref
# Test weakref.ref when used on an old-style class.

class C(object):

    def __init__(self, func):
        self.func = func

    def f(self):
        return self.func()

def somef():
    return "somef"

def somef_explicit():
    return "somef_explicit"

