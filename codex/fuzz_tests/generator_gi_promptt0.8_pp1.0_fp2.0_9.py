gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
test_gi_code(gi)
test_gi_frame(gi)

# Test that gi.gi_code is a method when it's a bound method
# and that gi.gi_frame is None when it's an unbound method
class X:
    def f(self):
        gi = (i for i in ())
        test_gi_code(gi, is_method=True)
        test_gi_frame(gi)
    @classmethod
    def g(cls):
        gi = (i for i in ())
        test_gi_code(gi, is_method=True)
        test_gi_frame(gi)
    @staticmethod
    def h():
        gi = (i for i in ())
        test_gi_code(gi)
        test_gi_frame(gi)

X().f()
X.g()
X.h()

# Test that gi.gi_code is a class when it's a class method
# and that gi.gi_frame is None when it's a
