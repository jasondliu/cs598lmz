fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi

def f():
    def g():
        return "ok"
    return g

def f_raises():
    def g():
        return "ok"
    yield from g

@jit
def jf():
    def g():
        return "ok"
    return g

@jit
def jf_raises():
    def g():
        return "ok"
    yield from g

def globals_contains(name):
    return name in globals()

@jit
def jglobals_contains(name):
    return name in globals()

@jit
def _pickle_code_obj(name):
    return pickle.dumps(globals()[name].__code__)


@jit
def _unpickle_code_obj(data):
    return pickle.loads(data)


class TestJitCompiledFunction(TestCase):
    def test_exception1(self):
        with self.assertRaises(TypeError) as raises:
            jglobals_cont
