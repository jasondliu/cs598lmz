from types import FunctionType
list(FunctionType(x,globals()) for x in y)
[functools.partial(function,y=x) for x in y]
[functools.partial(function, y=x)() for x in y]
[threading.Thread(target=function,args=(x,)).start() for x in y]
[threading.Thread(target=function,args=(x,)).start() for x in y]
[function(x) for x in y]
[function(x) for x in y]
[function(x) for x in y]
[function(x) for x in y]
[function(x) for x in y]
</code>
both of these should work.
Are you sure the problem is in this section of code?
if so, what does <code>f.value()</code> return?

