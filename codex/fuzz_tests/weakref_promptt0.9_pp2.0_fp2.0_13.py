import weakref
# Test weakref.ref(object)
# Test weakref.ref(type)


class C:
    pass


def callback(r):
    try:
        print "called"
    except:
        print "called"


r = weakref.ref(C, callback)
print r
print "live!" in dir(r)
print r()
print r() is C
print r() is C()
raw_input()
