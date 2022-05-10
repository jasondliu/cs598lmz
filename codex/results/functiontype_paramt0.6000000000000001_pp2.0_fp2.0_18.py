from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in a)

# or
[FunctionType(f.__code__, f.__globals__, name=f.__name__,
              argdefs=f.__defaults__,
              closure=f.__closure__) for f in a]
</code>
And the other way around:
<code>a = [f1, f2, f3]

# return list of ids
list(id(f) for f in a)

# or
[id(f) for f in a]
</code>
So the <code>list()</code> function is just a wrapper to convert any iterable to a list. 

