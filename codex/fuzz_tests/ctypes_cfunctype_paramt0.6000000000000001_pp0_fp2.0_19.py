import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

class my_callback:
    def __init__(self):
        self.fun =  FUNTYPE(self.callback)

    def callback(self, x):
        return x**2
</code>
However, I want to use this class in a function, so I would like to be able to do something like:
<code>def some_function(callback):
    #do something with callback

my_callback = my_callback()
some_function(my_callback)
</code>
I am not sure how to send the callback to the function, I have tried <code>some_function(my_callback.fun)</code> but it does not work.


A:

You can use <code>my_callback.fun</code> to obtain the <code>ctypes.CFUNCTYPE</code> instance, but you still need to pass the instance of <code>my_callback</code> to the function in order to make it callable.
In this case, you can just pass <code>my_callback</code> as the
