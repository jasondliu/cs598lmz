from types import FunctionType
list(FunctionType(c,globals(),'f')() for c in (compile(source,'','exec'),compile(source,'','eval')))
</code>

