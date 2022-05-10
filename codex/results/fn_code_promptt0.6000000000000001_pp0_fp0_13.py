fn = lambda: None
# Test fn.__code__.co_freevars
def test_freevars():
    def f():
        x = 1
        def g():
            return x
        return g
    assert f().__code__.co_freevars == ('x',)
    assert f().__closure__[0].cell_contents == 1
    def f():
        x = 1
        def g():
            def h():
                return x
            return h
        return g()
    assert f().__code__.co_freevars == ('x',)
    assert f().__closure__[0].cell_contents == 1

# Test fn.__defaults__
def test_defaults():
    def f1(a, b=2):
        return a+b
    assert f1.__defaults__ == (2,)
    def f2(a, b=2, c=3):
        return a+b+c
    assert f2.__defaults__ == (2, 3)
    def f3(a, b=2, c=3, d=4):
        return a
