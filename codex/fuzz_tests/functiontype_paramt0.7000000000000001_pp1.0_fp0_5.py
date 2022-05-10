from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)(a,b) for a,b in zip(data, data2))
</code>
What I need to do is run each of the functions in parallel within the list comprehension. Is there any way to do this?


A:

I think what you're looking for is the <code>multiprocessing</code> package. See the docs at https://docs.python.org/3/library/multiprocessing.html

