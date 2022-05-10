fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__module__ = '__main__'

class Bar(object):
    def __init__(self):
        self.flag = True
    def __str__(self):
        if self.flag:
            self.flag = False
            return 'Bar'
        return 'Baz'

def test_print_function():
    """Test the print_function option."""
    f = io.StringIO()
    with redirect_stdout(f):
        print_function(fn, print_function=print)
    print(f.getvalue())
    assert f.getvalue() == 'fn()\n'

def test_print_function_empty():
    """Test the print_function option."""
    f = io.StringIO()
    with redirect_stdout(f):
        print_function(fn, print_function=print)
    assert f.getvalue() == 'fn()\n'

