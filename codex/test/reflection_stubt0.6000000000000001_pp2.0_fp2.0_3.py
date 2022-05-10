fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


class TestCodeAttribute:

    def test_get_code_attribute(self):
        assert fn.__code__ == gi.gi_code

    def test_set_code_attribute(self):
        def fn():
            pass
        fn.__code__ = gi.gi_code
        assert fn.__code__ == gi.gi_code

    def test_delete_code_attribute(self):
        def fn():
            pass
        del fn.__code__
        assert fn.__code__ is None

    def test_code_attribute_on_non_function(self):
        class A:
            pass
        a = A()
        assert not hasattr(a, '__code__')
        raises(TypeError, setattr, a, '__code__', gi.gi_code)


class TestTracebackAttribute:

    def test_get_traceback_attribute(self):
        try:
            1 / 0
        except:
            tb = sys.exc_info()[2]
