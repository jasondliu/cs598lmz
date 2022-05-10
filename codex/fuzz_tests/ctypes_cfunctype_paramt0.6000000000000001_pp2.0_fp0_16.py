import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)

class MyTest(unittest.TestCase):
    def test_simple(self):
        """A simple test that checks whether the C++ interface works."""
        from cppimport.import_hook import import_hook
        import_hook.install()
        import test

        self.assertAlmostEqual(test.add(1.0, 2.0), 3.0)
        self.assertAlmostEqual(test.add(1.0, 3.0), 4.0)
        self.assertAlmostEqual(test.add(1.0, 4.0), 5.0)
        self.assertAlmostEqual(test.add(1.0, 5.0), 6.0)
        self.assertAlmostEqual(test.add(1.0, 6.0), 7.0)

    def test_simple_function_pointer(self):
        """A simple test that checks whether the C++ interface works."""
        from cppimport.import_hook import import_hook
       
