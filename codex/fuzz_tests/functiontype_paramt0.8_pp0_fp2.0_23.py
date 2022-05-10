from types import FunctionType
list(FunctionType(x.__code__, globals(), '', x.__defaults__, x.__closure__))
</code>
Here's my attempt - I'm sure there is a nicer way to do this.
<code>from types import FunctionType

def my_map(f, l):
    return list(FunctionType(f.__code__, globals(), '', f.__defaults__, f.__closure__)(a) for a in l)
</code>

