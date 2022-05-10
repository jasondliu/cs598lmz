import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with weakref callbacks
import weakref

class C:
    pass

callback_args = []

def callback(*args):
    print "weakref callback called with args", args
    callback_args.append(args)

obj = C()
wr = weakref.ref(obj, callback)

del obj
gc.collect()

assert callback_args == [(wr,)]

def callback_with_args(arg1, arg2, wr=weakref.ref(obj)):
    print "weakref callback with args called with args", arg1, arg2
    callback_args.append((arg1, arg2, wr))

obj = C()
wr = weakref.ref(obj, callback_with_args, "hello", "world")
callback_args[:] = []
del obj
gc.collect()

assert callback_args == [("hello", "world", wr)]

# Test that weakref callbacks are called in a predictable order
callback_args = []

class A:
    pass

class B(object):
    pass

class C(A
