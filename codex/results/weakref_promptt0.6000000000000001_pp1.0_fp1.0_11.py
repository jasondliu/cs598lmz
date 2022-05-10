import weakref
# Test weakref.ref(arg, callback)
def callback(w):
    print "callback called"
    print w
    print w()
    print w.__class__

w = weakref.ref(callback, callback)
print w
print w()
print w.__class__
print "done"
print '-'*20

# Test weakref.ref(arg, callback, (args...))
def callback2(w, arg):
    print "callback called"
    print w
    print w()
    print w.__class__
    print arg

w = weakref.ref(callback2, callback2, "hello")
print w
print w()
print w.__class__
print "done"
print '-'*20

# Test weakref.ref(arg, callback, [args...])
def callback3(w, arg):
    print "callback called"
    print w
    print w()
    print w.__class__
    print arg

w = weakref.ref(callback3, callback3, ["hello"])
print w
print w()
print w.__
