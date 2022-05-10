from types import FunctionType
list(FunctionType(lambda: a, {}, '', None, None).__globals__.items())

# outputs:
[('__builtins__', __builtins__)]

</code>
So it seems that that's the way attachments work in python. Is there a way to prevent this? We could use a class instead of a function, and in V8 I can check for these closures and throw, but I'm not sure how to do this with python. Is there an easier way? Thanks!


A:

<code>FunctionType(lambda: a, {}, '', None, None)</code> creates a function object using <code>a</code> as a closure variable. There is no way to prevent such a function being created.
If you don't have access to the code that creates the function object, then you can't prevent it, but you will be able to see that it refers to <code>a</code> as a closure variable and act accordingly. For example:
<code>if function.__name__ == '&lt;lambda&gt;' and function.__closure__:
    for var, value in function.__closure__:
