import weakref
# Test weakref.ref(x) with x being a builtin object with Weakref finalizers 
# and/or a destructor
# The list of such objects kept in this file is not exhaustive.
import gc
wrf = weakref.ref

# NB: Callbacks called by this test currently don't really check
# any property of their arguments.  If a new object type is added here
# that needs one of the callbacks to do more checking, add the
# corresponding function.  Each function can check whatever it wants.

def check_hashable(arg):
    hash(arg)

def check_nonzero(arg):
    if not arg:
        raise TypeError("object has zero identity")

checkers = {
    str: check_hashable,
    dict: check_hashable,
    tuple: check_hashable,
    list: check_nonzero,
    set: check_hashable,
    frozenset: check_hashable,
    # XXX specific numeric types?
}

