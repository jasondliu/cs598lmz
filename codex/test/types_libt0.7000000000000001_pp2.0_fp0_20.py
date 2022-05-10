import types
types.new_class("InlineTest", (object,), {})

class InlineTest(object):
    @jit.elidable
    def m1(self):
        return 42

    @jit.elidable
    def m2(self):
        return 42

    @jit.elidable_promote('all')
    def m3(self):
        return 42

    @jit.elidable_promote('all')
    def m4(self):
        return 42

class TestInline(BaseTest):
    def test_simple(self):
        def f():
            i = InlineTest()
            return i.m1()
        res = self.meta_interp(f, [])
        assert res == 42
        self.check_resops(guard_not_invalidated=4)
        #assert self.meta_interp.inline_short_preamble_ptr is not None

    def test_simple_again(self):
        def f():
            i = InlineTest()
            return i.m1()
        res = self.meta_inter
