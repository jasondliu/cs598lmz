import weakref
# Test weakref.ref(None) and weakref.ref(obj) with and without callback.

a = []

for t in ( None, None, None ):
    a.append( weakref.ref(t) )

print "Testing each of the three None references"
for r in a:
    print "  ", r, r()
    r == None

print "Testing the three None references"
for r in a:
    print "  ", r, r()
    r() == None

print "Testing the three None references again"
for r in a:
    print "  ", r, r()
    r() == None

print "Creating references to three objects"
a = []
for t in [None, 1, "abc"]:
    a.append( weakref.ref(t) )

print "Testing the three object references"
for r in a:
    print "  ", r, r()
    r() == None

print "Testing the three object references again"
for r in a:
    print "  ", r, r()
    r() == None

print "
