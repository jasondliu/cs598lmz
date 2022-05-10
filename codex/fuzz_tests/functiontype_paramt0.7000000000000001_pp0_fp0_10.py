from types import FunctionType
list(FunctionType(f.__code__, globals(), 'lambda').__globals__.keys())

f.__globals__['print'] = lambda *args: None
f.__globals__['raw_input'] = lambda: '2'
f()
</code>

