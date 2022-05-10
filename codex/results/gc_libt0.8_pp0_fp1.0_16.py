import gc, weakref



class RefCountingTests(unittest.TestCase):
    # A random set of refcounts for a string and for 'a'
    # Note that the numbers are "decreasing" in the sense that
    # the last number was the refcount *after* the previous
    # operation.
    STRING_REFCOUNTS = [9, 8, 7, 6, 4, 3, 2, 1, 2]
    ALIST_REFCOUNTS = [3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5,
                       4, 3, 2, 1, 0, 1, 2]

    def assertRefcountsEqual(self, obj, refcounts):
        rc = sys.getrefcount(obj)
        try:
            for val in refcounts:
                self.assertEqual(rc, val)
                # do something that should change refcount
                [obj]
                rc = sys.getrefcount(obj)
        finally:
            # Make sure that this
