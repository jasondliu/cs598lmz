import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect for collectable objects.

import gc, weakref
import StringIO
import sys

errors = 0

def remove_objects_with_finalizers():
    objects = set()
    for o in gc.get_objects():
        try:
            ref = weakref.finalize(o, lambda o=o: objects.add(o))
        except TypeError:
            pass
        else:
            ref.atexit = False
    gc.collect()
    return objects

infile, testout = sys.stdin, sys.stdout

try:
    f = weakref.finalize(StringIO.StringIO(), lambda s=sys.stdout: None)
    f.atexit = False

    outfile = StringIO.StringIO()
    try:
        sys.stdin, sys.stdout = open(__file__), outfile
        n = gc.collect()
    finally:
        sys.stdin, sys.stdout = infile, testout
    result = outfile.getvalue()
finally:
    sys.stdout =
