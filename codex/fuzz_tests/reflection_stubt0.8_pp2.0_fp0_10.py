fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__

# test_compile
fn = lambda: None
with raises(ValueError):
    compile(fn, '<test>', 'single')
compile('a, b = 1, 2', '<test>', 'single')
compile('a, b = 1, 2', '<test>', 'eval')
with raises(ValueError):
    compile('a, b = 1, 2', '<test>', 'exec')

# test_exec
def fn():
    a = 1
    b = 2
    exec('a, b = 1, 2')
    assert a == 1 and b == 2
fn()

# test_eval
fn = lambda: None
with raises(ValueError):
    eval([], fn.__globals__, fn.__globals__)
eval('[1, 2, 3]', fn.__globals__, fn.__globals__)

# test_dir
dir(None)
dir('')
dir(0)
dir(0.0)
dir(False)

