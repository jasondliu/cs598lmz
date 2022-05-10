import gc, weakref

def am_testing ():
    return sys.argv[0].endswith ('check.py')

# When running unit tests, it's nice to be able to see when the cached
# data is being looked at.
verbose_cache = False

# In the non-test case, we still want to make sure there aren't any
# references to the cached data lying around, so if there are, we
# print a warning.
print_gc_warnings = False

class _CacheBase (object):
    """Base class for dbusmock caches."""

    def __init__ (self, reset_cb):
        self._reset_cb = reset_cb
        self._reset_blocked = False
        self._reset_blocked_refs = []
        self._reset()

    def _reset (self):
        self._enable_reset (False)
        for r in self._reset_blocked_refs:
            r.destroy ()
        self._reset_blocked_refs = []

        self._clear_cache ()
