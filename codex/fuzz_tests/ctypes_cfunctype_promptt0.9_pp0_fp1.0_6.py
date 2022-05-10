import ctypes
# Test ctypes.CFUNCTYPE().

class Test(BaseTestChecker):
    def test_callable(self):
        def f():
            pass
        self.assertEqual(callable(f), True)
      
