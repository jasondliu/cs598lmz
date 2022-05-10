import weakref
# Test weakref.ref(s) is an instance of the type, but then only
# a weakref.ReferenceType, not a weakref.WeakSet in this case.
import weakref
import sys
try:
    from weakrefset import WeakSet
except ImportError:
    WeakSet = None

if WeakSet is None:
    raise Exception("Could not import weakrefset.weakset")

class MyInt(int):
    pass

class MyStr(str):
    pass

def check_in_out(SetType, seq, verbose=0):
    try:
        ws = SetType(seq)
        if verbose:
            print "Constructed from:", seq
            print "weakset:", ws
    except TypeError:
        if verbose:
            print "No construction from:", seq
        return

    count = 0
    for obj in seq:
        if obj in ws:
            count += 1
        else:
            raise TestFailed, "expected %s in set" % `obj`

    if count != len(seq):
        raise TestFailed, "%
