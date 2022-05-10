fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print fn()
fn.__code__ = [None]
print fn()
fn.__code__ = range(5)
print fn()
fn.__code__ = xrange(5)
print fn()
fn.__code__ = (1,2,3,4)
print fn()
fn.__code__ = (1,2,3,4)
print fn()
fn.__code__ = {'a':1, 'b':2}
print fn()
fn.__code__ = {'a':1, 'b':2}
print fn()
"""

# test_unpack_tuple_with_iter()

"""
# This uses the new CPython exception handling system.

def test_unpack_tuple_with_iter_2():
    fn = lambda: None
    fn.__code__ = lambda: None
    try:
        fn()
    except TypeError:
        print "1"
    fn.__code__ = [None]
    try:
        fn()
    except TypeError:
        print "2"
   
