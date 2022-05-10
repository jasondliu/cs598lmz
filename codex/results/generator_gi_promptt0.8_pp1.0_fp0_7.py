gi = (i for i in ())
# Test gi.gi_code, introduced in Python 2.6.
gi.gi_code

# Test tuple.index, added in Python 2.6.
(1).index(1)

# Test tuple.count, added in Python 2.6.
(1).count(1)

# Python 2.6 introduced some new methods on dict.
dict = {}
# Test dict.iterkeys, added in Python 2.6.
for key in dict.iterkeys(): pass
# Test dict.itervalues, added in Python 2.6.
for value in dict.itervalues(): pass
# Test dict.iteritems, added in Python 2.6.
for key, value in dict.iteritems(): pass
# Test dict.viewkeys, added in Python 2.6.
dict.viewkeys()
# Test dict.viewvalues, added in Python 2.6.
dict.viewvalues()
# Test dict.viewitems, added in Python 2.6.
dict.viewitems()

# Python 2.6 introduced sys.getsizeof, which has a different signature to the
# size_of function in the unittest module
