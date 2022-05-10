from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, name='foo',
                  argdefs=f.func_defaults, closure=f.func_closure)
     for f in functions)
# [foo]
</code>

