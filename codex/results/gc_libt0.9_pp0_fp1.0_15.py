import gc, weakref
lastref = None

def _fork():
    global lastref
    for i in range(5):
        c = weakref.ref(allocate())
        if lastref is not None and lastref() is not None:
            return False
        lastref = c
    return True

class BaseTest(TestCase):

    def test_gc(self):
        # Issue #10438: if the old or new value of an object has a finalizer,
        # that finalizer is called during the minor collection when the object
        # is moved.  This test checks that the finalizer of the old value is
        # run before the finalizer of the new value.

        L = []
        record = L.append

        innerblock = None
        outerblock = None
        ref = asyncio.SafeChildWatcher()

        class C:
            def __del__(self):
                record("deleting " + str(self))
                if len(L) == 2:
                    # First delete.  Schedule and then delete the second
                    # delete.
                    innerblock.set()
                    outer
