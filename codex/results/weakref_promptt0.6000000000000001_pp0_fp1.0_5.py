import weakref
# Test weakref.ref()

def test():
    print "In test()"
    print "Creating a weakref to None"
    r = weakref.ref(None)
    print "Checking the weakref"
    print r() is None
    print "Checking the weakref after clearing"
    r = None
    print "Checking the weakref after clearing again"
    print r() is None
    print "In test()"
    print "Creating a weakref to a list"
    l = [1, 2, 3]
    r = weakref.ref(l)
    print "Checking the weakref"
    print r() is l
    print "Checking the weakref after clearing"
    l = None
    print r() is None
    print "Checking the weakref after clearing again"
    print r() is None
    print "In test()"
    print "Creating a weakref to a dictionary"
    d = {'a': 'b'}
    r = weakref.ref(d)
    print "Checking the weakref"
    print r() is d
   
