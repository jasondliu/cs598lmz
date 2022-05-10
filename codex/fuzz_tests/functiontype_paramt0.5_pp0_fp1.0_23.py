from types import FunctionType
list(FunctionType(f.__code__, globals(), 'foo') for f in (foo, bar))
</code>

