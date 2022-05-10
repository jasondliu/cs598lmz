import weakref
# Test weakref.ref(traceback.extract_stack()).
# This could fail due to the garbage collector discarding the stack frame
# from which the weakref is created, or because traceback.extract_stack()
# returns frames that are not directly reachable from the stack frame from
# which the weakref is created.
# The test passes on CPython.
seen = set()
def f(depth=1):
    if depth > 2:
        return
    extract_stack = traceback.extract_stack
    frm = extract_stack()[-1]
    seen.add(weakref.ref(frm))
    f(depth+1)
f()
if len(seen) != 3:
    print(len(seen), 'weak references to traceback frames have survived')

# Check that __sizeof__() is independent of the memo
# http://bugs.python.org/issue1413
import sys
if sys.version_info >= (2, 7):
    tb = traceback.extract_stack()
    del tb.tb_frame
    size1 = sys.getsize
