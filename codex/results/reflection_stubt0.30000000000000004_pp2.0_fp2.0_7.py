fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #20897: __code__ attribute of built-in methods
def check_builtin_method(name):
    method = getattr(int, name)
    code = method.__code__
    assert code.co_argcount == 1
    assert code.co_varnames == ('self',)
    assert code.co_name == name
    assert code.co_filename == '<built-in method %s of int object>' % name
    assert code.co_firstlineno == 1
    assert code.co_lnotab == b''

for name in ('__abs__', '__add__', '__and__', '__bool__', '__ceil__',
             '__divmod__', '__eq__', '__floor__', '__floordiv__', '__ge__',
             '__gt__', '__index__', '__int__', '__invert__', '__le__', '__lshift__',
             '__lt__', '__mod__', '__mul__', '__neg
