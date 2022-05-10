from types import FunctionType
list(FunctionType(c.__code__, globals(), 'c'))
</code>

