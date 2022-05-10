fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(gi.gi_code)()
fn()
""")


def test_cpython_bug_19667_py33():
    """
    CPython 3.3 segfaults when a generator function has an empty
    code object.
    """
    with pytest.raises(TypeError):
        run_python_module('''
def fn():
    yield
fn.__code__ = type(fn.__code__)()
list(fn())
''')


@pytest.mark.skipif(sys.version_info[:2] < (3, 3),
                    reason='requires Python 3.3+')
def test_cpython_bug_19667_py34():
    """
    CPython 3.4- segfaults when a generator function has an empty
    code object.
    """
    with pytest.raises(TypeError):
        run_python_module('''
def fn():
    yield
fn.__code__ = type(fn.__code__)()
list(fn())
''')


def test_cpython
