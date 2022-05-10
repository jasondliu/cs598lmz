import types
# Test types.FunctionType as an implicit base class for user-defined functions.
#
# Requires the class Tree with methods walk and count_fns
#
class FunctionTypeTest(unittest.TestCase):
    def test_function_type_base(self):
        # --------------------------------------------------  test function
        def f(): pass
        def g(a): return a
        def h(a, b, c=0, d=0, e=0): return a+2*b+3*c+4*d+5*e
        def rec(a):
            if a > 0:
                return rec(a - 1)
            else: return 0
        # -------------------------------------------------------  expected
        expected_f = "/f\n"
        expected_g = "/g\n .a\n"
        expected_h = "/h\n .a .b .c .d .e\n"
        expected_rec = "/rec\n .a\n"
        expected_walk_f = [expected_f]
        expected_walk_g = [expected_g]
        expected_walk_h = [expected
