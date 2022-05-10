from types import FunctionType
list(FunctionType(f.__code__, g.__globals__, name='foo',
                  argdefs=f.__defaults__,
                  closure=f.__closure__)() for f in (cls.__init__, cls.__new__))
</code>
I think this will work.
For examples see <code>types.FunctionType</code>
<code>FunctionType(code, globals[, name[, argdefs[, closure]]])
</code>
You will have to replace <code>globals</code> with <code>f.__globals__</code>

