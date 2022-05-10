from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (f1, f2, f3, f4))
</code>
The <code>FunctionType</code> constructor doesn't take a <code>__closure__</code> argument though, so you'll have to manually add it to the created function afterwards.

