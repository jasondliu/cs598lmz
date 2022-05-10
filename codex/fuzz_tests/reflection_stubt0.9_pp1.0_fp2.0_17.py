fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


def _freeze_func(func, _frozen=frozenset):
    """Recursively freezes the code objects in the func's closure.
    """

    def freeze():
        func.__code__ = _frozen(func.__code__)
        for c in findclosurevars(func):
            if c.cell_contents is not None:
                c.cell_contents = _freeze_func(c.cell_contents)
        return func
    return freeze


@_freeze_func
def _call_function_objargs(func, args=None, kw=None):
    return func(*(args or ()), **(kw or {}))


def _call_function_object(func, *args, **kw):
    if kw:
        return func(*args, **kw)
    else:
        try:
            return func(*args)
        except TypeError:
            exc_info = sys.exc_info()
            try:
                return _call_function_objargs(func, args)

