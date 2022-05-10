fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi, fn

CodeType_add_flag(lambda: None, 'CO_HIDDEN_ATTR', 0x1000)
CodeType_add_flag(lambda: None, 'CO_GETATTR_FLAGS', 0x2000)

_flag_names = set()


def CodeType_add_flag(cls, name, value):
    """Adds a CodeType flag."""
    setattr(cls, name, value)
    _flag_names.add(name)


def CodeType_pretty_flags(flags, flag_names=_flag_names):
    """Returns a pretty representation of the flags."""
    return ', '.join(n for n in flag_names if getattr(flags, n, False))


def get_instructions(func):
    """Returns the bytecode instructions for the given function.

    For example, this function would return the bytecode for `mako.runtime.StrictUndefined.__mod__`.
    """
    with PY3:
        if isinstance(func, (type, classmethod)):

