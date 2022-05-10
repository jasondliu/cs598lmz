fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi
copyreg.pickle(types.FunctionType, _reduce_ex)

##
# Register ourselves for pickling time-related types.

_dispatch_table = {}

def _reduce_time(x, state=None):
    arg = x.timetuple() + (x.microsecond,)
    f = _dispatch_table.get(x.__class__)
    if f:
        rv = f(arg, state)
    else:
        rv = (_rebuild_time, (x.__class__, arg))
    return (rv, _time_state)

def _reduce_time_subclass(x, state=None):
    arg = x.timetuple() + (x.microsecond,)
    f = _dispatch_table.get(type(x))
    if f:
        rv = f(arg, state)
    else:
        rv = (_rebuild_time, (x.__class__, arg))
    return (_rebuild_time, (x.__class
