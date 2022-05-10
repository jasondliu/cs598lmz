import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    pass

def callback(obj):
    print "Callback called with", obj
    print "Callback called with", obj.__class__

def callback2(obj):
    print "Callback2 called with", obj
    print "Callback2 called with", obj.__class__

def callback3(obj):
    print "Callback3 called with", obj
    print "Callback3 called with", obj.__class__

def callback4(obj):
    print "Callback4 called with", obj
    print "Callback4 called with", obj.__class__

def callback5(obj):
    print "Callback5 called with", obj
    print "Callback5 called with", obj.__class__

def callback6(obj):
    print "Callback6 called with", obj
    print "Callback6 called with", obj.__class__

def callback7(obj):
    print "Callback7 called with", obj
    print "Callback7 called with", obj.__class__

def callback8(obj):
    print "Callback8 called with", obj
    print "Callback
