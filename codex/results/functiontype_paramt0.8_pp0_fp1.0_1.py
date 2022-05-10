from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# Two
def func(x):
    return x
list(func for x in range(10))

# Three
# This is the only way to create a lambda function.
list((lambda x=x: x)() for x in range(10))

# Four
list((lambda x: x)(x) for x in range(10))
</code>
Example 2:
<code># One
from types import FunctionType
def func(x):
    return x
list(FunctionType(func.__code__, globals(), 'func', func.__defaults__, func.__closure__) for x in range(10))

# Two
def func(x):
    return x
list(func for x in range(10))

# Three
list((lambda x=x: x)() for x in range(10))

# Four
list((lambda x: x)(x) for x in range(10))
</code>
Result:
<code>[&lt;function &lt;lambda&gt; at
