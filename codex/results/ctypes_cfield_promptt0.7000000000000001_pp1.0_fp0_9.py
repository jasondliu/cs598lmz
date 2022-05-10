import ctypes
# Test ctypes.CField
import ctypes.test.test_cfiled

# _________________________________________________________________

class __TestGc(object):
    def test_simple(self):
        import gc
        l = []
        l.append(l)
        gc.collect()
        del l
        gc.collect()

    def test_cycle(self):
        import gc
        class A:
            pass
        a = A()
        a.a = a
        gc.collect()
        del a
        gc.collect()

    def test_callback(self):
        import gc
        class B(object):
            def __del__(self):
                pass

        class A(object):
            def __del__(self):
                self.b = B()
                gc.collect()
                del self.b

        a = A()
        a.b = B()
        del a
        gc.collect()
        gc.collect()
        gc.collect()

    def test_callback_with_finalizer(self):
        import gc
        class
