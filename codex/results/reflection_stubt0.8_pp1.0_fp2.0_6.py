fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
gi.gi_running = 0
gi.gi_frame = fn.__code__
gi.gi_code = fn.__code__
''' % ())


def test_noniterable_generator():
    fn = raises(TypeError, run, '''
def f(): yield 1
''')
    assert str(fn) == '<unbound method f.<locals>.<genexpr> at 0x%x>' % fn.__code__.co_firstlineno


def test_iter_unpack_bug():
    run('''
def f(): yield 1, 2
x = list(f())
''')


def test_generator_return_with_value():
    fn = raises(SyntaxError, run, '''
def f(): yield; return 1
''')
    assert str(fn) == '<function f at 0x%x>' % fn.__code__.co_firstlineno


def test_yield_from():
    fn = run('''
def f(): return (i for i in range(10))
def g
