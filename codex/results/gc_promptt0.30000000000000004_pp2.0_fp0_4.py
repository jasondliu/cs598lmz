import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakrefs

class Foo(object):
    pass

def callback(w):
    print "callback"

def callback2(w):
    print "callback2"

def callback3(w):
    print "callback3"

def callback4(w):
    print "callback4"

def callback5(w):
    print "callback5"

def callback6(w):
    print "callback6"

def callback7(w):
    print "callback7"

def callback8(w):
    print "callback8"

def callback9(w):
    print "callback9"

def callback10(w):
    print "callback10"

def callback11(w):
    print "callback11"

def callback12(w):
    print "callback12"

def callback13(w):
    print "callback13"

def callback14(w):
    print "callback14"

def callback15(w):
    print "callback15"

def callback16(w):
    print "callback16"


