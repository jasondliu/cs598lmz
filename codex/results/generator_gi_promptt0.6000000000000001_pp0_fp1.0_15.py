gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'
# Test gi.gi_frame.f_code.co_name
assert gi.gi_frame.f_code.co_name == 'test_gen_code'

# Test __class__
def test_cls():
    class C:
        x = 42
        def __init__(self):
            self.x = 43
    c = C()
    assert c.__class__ == C
    assert c.x == 43
    # test __class__ in function
    def f():
        return c.__class__
    assert f() == C
    # test __class__ in class
    class D:
        cls = c.__class__
    assert D.cls == C
    # test __class__ in function in class
    class E:
        def f(self):
            return c.__class__
    assert E().f() == C

# Test __del__
class D:
    def __del__(self):
        self.de
