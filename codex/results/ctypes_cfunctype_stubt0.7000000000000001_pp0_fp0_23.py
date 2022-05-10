import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
"""

class TestPyGC(TestCase):
    run_test_with_all_cpython_versions = True
    run_test_with_pyston = True

    def test_simple(self):
        import sys
        import gc
        gc.collect()
        #print(gc.get_stats())
        self.assertEqual(gc.get_count(), (0, 0, 0))
        class A(object):
            pass
        a = A()
        self.assertEqual(gc.get_count(), (1, 0, 0))
        self.assertTrue(a in gc.get_objects())
        self.assertFalse(A in gc.get_objects())

        del a
        gc.collect()
        self.assertEqual(gc.get_count(), (0, 0, 0))

        #print(gc.get_stats())
        gc.set_debug(gc.DEBUG_STATS)
        #print(gc.get_stats())
        gc.set_debug(0)

        # with g
