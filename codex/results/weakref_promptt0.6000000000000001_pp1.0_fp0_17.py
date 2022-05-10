import weakref
# Test weakref.ref() with callbacks

class A(object):
    def __del__(self):
        print "deleting A"

def callback(r):
    print "callback"

r = weakref.ref(A(), callback)

del r

print "DONE"
