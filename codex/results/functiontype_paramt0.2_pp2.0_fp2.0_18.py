from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# TypeError: 'lambda' is not a valid non-string sequence or mapping object
</code>

