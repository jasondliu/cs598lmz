from types import FunctionType
list(FunctionType(code, globals(), name)())
</code>
this will give you the output you need.

