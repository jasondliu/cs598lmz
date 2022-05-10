fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27076: __code__ attribute of a builtin function should be None
def check_builtin_code(name):
    f = getattr(builtins, name)
    assert f.__code__ is None

check_builtin_code('abs')
check_builtin_code('min')
check_builtin_code('max')
check_builtin_code('round')
check_builtin_code('sorted')

# Issue #27076: __code__ attribute of a method should be None
def check_method_code(name):
    f = getattr(int, name)
    assert f.__code__ is None

check_method_code('__add__')
check_method_code('__sub__')
check_method_code('__mul__')
check_method_code('__floordiv__')
check_method_code('__mod__')
check_method_code('__divmod__')
check_method_code('__pow__')
check_method_code('__lshift__
