fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: None)()
fn.__code__.co_filename = gi.gi_code.co_filename = ''
fn.__code__.co_firstlineno = gi.gi_code.co_firstlineno = 0
fn.__code__.co_name = gi.gi_code.co_name = ''
fn.__code__.co_code = gi.gi_code.co_code = b''

pytest.register_assert_rewrite('_pytest.assertion.rewrite')
pytest.register_assert_rewrite('_pytest.assertion.util')


def pytest_pycollect_makeitem(collector, name, obj):
    if collector.funcnamefilter(name):
        if not callable(obj):
            return
        item = pytest.Function(name, parent=collector)
        if '()' not in item.name:
            item._ishidden = True
        return list(collector._genfunctions(name, obj))


def pytest_pyfunc
