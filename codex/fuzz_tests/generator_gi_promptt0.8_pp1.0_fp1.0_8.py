gi = (i for i in ())
# Test gi.gi_code
print
print "Doing next() on spare generator"
print "Result:", next(gi)
print "Cleaning up"
print "Result:", gi.gi_code
print
print

# Test gi_frame on non-empty spare generator
gi = (i for i in [1,2,3])
# Test gi.gi_code
print
print "Doing next() on spare generator"
print "Result:", next(gi)
print "Cleaning up"
print "Result:", gi.gi_code
print
print


# Test gi_frame on spare generator which still has __iter__
gi = (i for i in [1,2,3])
for i in range(3): next(gi)
# Test gi.gi_code
print
print "Doing next() on spare generator"
try:
    print "Result:", next(gi)
except StopIteration:
    print "Caught StopIteration"
print "Cleaning up"
print "Result:", gi.gi_code
print
print


# Test gi
