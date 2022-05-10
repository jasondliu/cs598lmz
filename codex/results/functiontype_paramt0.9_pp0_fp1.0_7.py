from types import FunctionType
list(FunctionType(function.__code__, function.__globals__, name=function.__name__,
                  argdefs=function.__defaults__, closure=function.__closure__)() for function in functions)
</code>
but this is not what I want as I do not want to call the functions. I just want
to order list of functions by the number of argument.


A:

<code>functions.sort(key=lambda function: function.__code__.co_argcount)
</code>

