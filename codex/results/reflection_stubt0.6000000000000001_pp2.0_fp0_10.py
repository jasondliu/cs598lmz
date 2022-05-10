fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi)()
fn.__code__.co_filename = gi.gi_code.co_filename = "<test>"
fn.__code__.co_firstlineno = gi.gi_code.co_firstlineno = 1
gi.gi_code.co_name = "<genexpr>"

def test_trace_generator_expression():
    tb = traceback.TracebackException(type(None), None, fn)
    assert tb.stack == [(fn.__code__, 1)]
    assert tb.stack[0].line == "<genexpr> = <genexpr>()"
    with captured_stdout() as output:
        print(tb)
    assert output.getvalue() == 'None\n'

# Issue #14239
def test_trace_generator_expression_with_tuple_unpacking():
    def fn():
        _, _ = (i for i in ())
    tb = traceback.TracebackException(type(None), None, fn)
    assert tb.stack
