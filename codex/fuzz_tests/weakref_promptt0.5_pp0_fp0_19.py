import weakref
# Test weakref.ref() with callbacks

class Foo(object):
    pass

def callback(w):
    global n
    n -= 1
    print "callback", w, n

def callback2(w):
    global n
    n -= 1
    print "callback2", w, n

def callback3(w):
    global n
    n -= 1
    print "callback3", w, n

def callback4(w):
    global n
    n -= 1
    print "callback4", w, n

def callback5(w):
    global n
    n -= 1
    print "callback5", w, n

def callback6(w):
    global n
    n -= 1
    print "callback6", w, n

def callback7(w):
    global n
    n -= 1
    print "callback7", w, n

def callback8(w):
    global n
    n -= 1
    print "callback8", w, n

def callback9(w):
    global n
    n -= 1
    print "callback9", w, n
