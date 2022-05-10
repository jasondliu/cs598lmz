fn = lambda: None
gi = (i for i in ())
fn.__code__ = 42
gi.gi_frame = fn
gi.gi_frame.f_locals = {'ld': object, 'chconv': object, 'gi_frame': object, '__name__': 'code', '__doc__': None, '__package__': None, '__annotations__': {}, '__qualname__': 'code', 'chunksize': 4, 'ldcmp': object, 'chunk': object, 'fn': <function <lambda> at 0x7f2a016a93a8>, 'CodeType': <class 'code.CodeType'>, '_codecs': <module 'codecs' from '/usr/lib/python3.6/codecs.py'>, '_': <function atexit.register(func, *targs, **kargs)>, '__': <function atexit.unregister(func)>, '___': <function atexit._run_exitfuncs()>, '_exit': <function sys.exit(status)>, '_codecs_cn': <module '_codecs_cn' from '/usr/lib/python3.6/_
