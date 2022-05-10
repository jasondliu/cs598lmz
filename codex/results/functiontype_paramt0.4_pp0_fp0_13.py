from types import FunctionType
list(FunctionType(code, globals(), name=name,
                  argdefs=argdefs, closure=closure))
</code>

