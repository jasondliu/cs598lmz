import types
types.ClassType = type

class Test(unittest.TestCase):
    def test_class(self):
        class A(object):
            pass
        class B(object):
            pass
        class C(A):
            pass
        class D(A):
            pass
        class E(C):
            pass
        class F(D):
            pass
        self.assertEqual(issubclass(A, A), True)
        self.assertEqual(issubclass(A, B), False)
        self.assertEqual(issubclass(A, C), False)
        self.assertEqual(issubclass(A, D), False)
        self.assertEqual(issubclass(A, E), False)
        self.assertEqual(issubclass(A, F), False)
        self.assertEqual(issubclass(B, A), False)
        self.assertEqual(issubclass(B, B), True)
        self.assertEqual(issubclass(B, C), False)
        self.assertEqual(
