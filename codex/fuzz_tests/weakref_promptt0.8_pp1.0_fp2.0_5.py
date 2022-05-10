import weakref
# Test weakref.ref(None) == None

fail = 0

try:
    a = weakref.ref(None)
    if a != None:
        print "weakref.ref(None) was not None"
        fail = 1
except TypeError, e:
    print "Caught TypeError:", e
    fail = 1

try:
    # Chec
