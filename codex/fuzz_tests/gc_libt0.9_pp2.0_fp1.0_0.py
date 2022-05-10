import gc, weakref, types

class TestGC(unittest.TestCase):
    def callback(self, ignored):
        self.callback_called += 1

    def test_create_cycle_with_finalizer(self):
        self.callback_called = 0
        def f():
            pass
        obj = Finalize(C(), f)
        wr = weakref.ref(C(), self.callback)
        a = A()
        refs = [
            weakref.ref(a)
        ]

        for i in range(10):
            c1 = C()
            c2 = C()
            refs.append(weakref.ref(c1))
            refs.append(weakref.ref(c2))
            c1.cycle = c2
            c2.cycle = c1
        wr = weakref.ref(a, self.callback)
        del a
        obj.atexit = lambda : None
        gc.collect()
        for wr in refs:
            if wr() is not None:
                break
        else:
            self.assertEqual(
