from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f') 
     for f in (lambda: a, lambda: b))

# [<function <lambda> at 0x109bcc730>, <function <lambda> at 0x109bcc7b8>]
</code>

