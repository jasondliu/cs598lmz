import weakref
# Test weakref.ref with C API

# This is a modified version of weakref_cobject.py.  The types tested
# aren't supported by all Python builds.

import test.test_support
import weakref
import UserDict

# the event callback is called with a list of all registered callbacks
# and a list of all dead callbacks
def event(arg):
    # arg is a list of callbacks and dead callbacks
    print 'event:', arg
    all = arg
    arg = all()

    print 'event: callbacks count, dead count =', len(arg[0]), len(arg[1])

    if len(arg[1]): print 'dead callbacks:'
    for x in arg[1]:
        print x,
    print

    if len(arg[0]): print 'alive callbacks:'
    for x in arg[0]:
        print x,
    print

def make_key(o, k):
    return str(id(o)) + ':' + k

class WeakValueDictionary(UserDict.UserDict):

    def __init
