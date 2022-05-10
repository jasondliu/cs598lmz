import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a weakref callback

import unittest
from test.support import run_unittest

class Test(unittest.TestCase):
    def test_callback(self):
        # Check that weakref callbacks are called at the right time
        # and with the right arguments.
        callback_args = []
        def callback(obj):
            callback_args.append(obj)
        class A:
            pass
        a = A()
        a.b = A()
        a.b.a = a
        wr = weakref.ref(a, callback)
        del a
        gc.collect()
        self.assertEqual(callback_args, [])
        gc.collect()
        self.assertEqual(callback_args, [wr])
        del a
        gc.collect()
        self.assertEqual(callback_args, [wr])

def test_main():
    run_unittest(Test)

if __name__ == "__main__":
    test_main()
