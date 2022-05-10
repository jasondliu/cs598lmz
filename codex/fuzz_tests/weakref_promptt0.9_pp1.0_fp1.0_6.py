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

def f():
    print "hi"

c = weakref.ref(C(somef), f)
c_explicit = weakref.ref(C(somef_explicit), f)
x = c()
y = c_explicit()
import gc
gc.collect()
print "c():  ", c()  # returns a dead ref
print "c():  ", c() is None
print "c_explicit():", c_explicit()  # returns None
print "c_explicit():", c_explicit() is None

# Test __call__ can take an argument list

def someFunc(arg1, arg2, kwd='default'):
    print arg1, arg2, kwd

w
