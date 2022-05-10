fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__name__ = 'fn'
try:
    fn()
except RuntimeError as e:
    assert e.args == ('generator cannot be called',)
else:
    assert False, 'did not raise'

# GeneratorExit

def gen():
    yield
    try:
        yield
    except GeneratorExit:
        print('GeneratorExit')

g = gen()
next(g)
g.close()
