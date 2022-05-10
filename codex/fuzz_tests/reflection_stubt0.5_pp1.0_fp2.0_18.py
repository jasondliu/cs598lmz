fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = gi.gi_name
fn.__doc__ = gi.gi_doc
fn.__module__ = gi.gi_module
fn.__dict__ = gi.gi_frame.f_locals

def _get_func(obj):
    if isinstance(obj, types.FunctionType):
        return obj
    if isinstance(obj, types.MethodType):
        return obj.__func__
    return None

def _get_code(obj):
    func = _get_func(obj)
    if func is not None:
        return func.__code__
    return None

def _get_func_or_code(obj):
    func = _get_func(obj)
    if func is not None:
        return func
    return _get_code(obj)

def _get_module(obj):
    func = _get_func(obj)
    if func is not None:
        return func.__module__
    code = _get_code(obj)
    if code
