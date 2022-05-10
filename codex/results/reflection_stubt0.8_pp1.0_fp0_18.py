fn = lambda: None
gi = (i for i in ())
fn.__code__ = CodeType(0, 0, 0, 0, 0, b'', (), (), (), "", "", 0, b"")
fn.__code__.co_firstlineno = 1
inspect.currentframe = _dummy = lambda *args: fn
inspect.getframeinfo = lambda frame, context=1: (frame.f_code, frame.f_lineno)
linecache.getline = lambda filename, lineno, module_globals=None: ''
sys.version_info = (3,)
sys.version = ".".join(map(str, sys.version_info[:2])) + " dummy"
sys.platform = ''

if sys.version_info[0] > 2:
    import builtins
    range = builtins.range
else:
    import __builtin__
    range = __builtin__.range

def __dir__(obj):
    if isinstance(obj, Module):
        return sorted(name for name in obj.__dict__
                      if not (name.startswith('_') or name == 'this'))
   
