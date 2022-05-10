fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# Issue #15963: The code object of a generator should not be writable.
def test_generator_code_is_not_writable():
    def gen():
        yield 1
    g = gen()
    with raises(TypeError):
        g.gi_code = None

def test_generator_code_is_not_writable_2():
    def gen():
        yield 1
    g = gen()
    with raises(TypeError):
        del g.gi_code

def test_generator_code_is_not_writable_3():
    def gen():
        yield 1
    g = gen()
    with raises(TypeError):
        g.gi_code = None

def test_generator_code_is_not_writable_4():
    def gen():
        yield 1
    g = gen()
    with raises(TypeError):
        del g.gi_code

def test_generator_code_is_not_writable_5():
    def gen():
        yield 1
    g = gen
