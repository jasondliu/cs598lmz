fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = namedtuple('Code', 'co_name')('__init__')
gi.gi_frame = namedtuple('Frame', 'f_locals')({})
setattr(fn, '__globals__', gi.gi_frame.f_locals)
fn.__module__ = '__main__'
