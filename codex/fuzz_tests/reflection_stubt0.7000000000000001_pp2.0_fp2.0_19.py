fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(None)()
fn.__code__.co_lnotab, gi.gi_frame.f_lasti = '', 0
print(hasattr(fn, '__code__'))  # True
print(hasattr(fn, 'func_code'))  # True
print(hasattr(gi, 'gi_code'))  # True
print(hasattr(gi, '__code__'))  # True
print(hasattr(fn, '__closure__'))  # True
print(hasattr(fn, 'func_closure'))  # True
print(hasattr(fn, '__defaults__'))  # False
print(hasattr(fn, 'func_defaults'))  # False
print(hasattr(fn, '__globals__'))  # False
print(hasattr(fn, 'func_globals'))  # False
print(hasattr(fn, '__name__'))  # False
print(hasattr(fn, 'func_name'))  # False
try:
   
