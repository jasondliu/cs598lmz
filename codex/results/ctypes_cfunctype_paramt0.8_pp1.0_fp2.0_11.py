import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)


@functools.wraps(func)
def wrapper(*args, **kwargs):
    callback = FUNTYPE(func)
    return lib.register_callback(callback, *args, **kwargs)
return wrapper
</code>
In the example above, <code>wrapped_register_callback</code> accepts a function as an argument and returns another function. This allows me to decorate the original <code>register_callback</code> function with <code>@wrapped_register_callback</code>, like so:
<code>lib = ctypes.CDLL('libpython_wrapper.so')

@wrapped_register_callback
def my_callback():
    print 'Hello, world!'
</code>
Now I can call <code>lib.register_callback</code> as before and it will automatically be wrapped.

