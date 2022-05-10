import weakref
# Test weakref.ref as needed.
supports_weakref = lambda: True

from guppy.heapy.test.support import gc_collect

def my_repr(self):
    return '<%s.%s #%d at %r>' % (
        self.__class__.__module__,
        self.__class__.__name__,
        self.__index__(),
        self.__key__())

def _do_test_live_set(live_set):
    live_set.__index__()
    live_set.__key__()
    unittest.TestCase.assertEqual(live_set.__repr__(), my_repr(live_set))
    ref = weakref.ref(live_set)
    live_set = None
    gc_collect()

global ref_set
global no_index_set
global key_set
global index_set
global index_ext_set
global index_ext_key_set
global items_set
global items_ext_set
global items_ext_key_set

