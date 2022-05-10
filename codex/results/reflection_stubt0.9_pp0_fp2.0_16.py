fn = lambda: None
gi = (i for i in ())
fn.__code__ = CodeType(0, 0, 0, 1, 0, b'', (), (), (var_,), '', '', 0, b'')
var_.__annotations__ = {"" : gi}
fn()
"""
        out, err, exitcode = assert_python_failure(code)
        assert re.search('RuntimeError: generator ignored GeneratorExit', err)

class AppTestCoro(CoroTests):
    def setup_class(cls):
        if not hasattr(cls, 'space'):    # PyPy
            cls.space = gettestobjspace(usemodules=('_continuation',))
        cls.w_runappdirect = cls.space.wrap(runappdirect)

    def test_init_exc(self):
        if not self.runappdirect:
            skip("__init__ raises outside direct call")
            # See docstring of CoroTests.test_init_exc
        exc = ValueError()
        raises(ValueError, coroutine(lambda: None).__init__, exc)

        def g():
            yield
