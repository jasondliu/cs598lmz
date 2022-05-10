import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print fun.__name__
</code>
This prints <code>fun</code> as expected.
Now, if I make a class with a <code>__call__</code> method,
<code>class Fun(object):
    def __call__(self):
        return 42

print Fun().__name__
</code>
This prints <code>__call__</code>.
How can I make a class with a <code>__call__</code> method that looks like a function? Is there a way to make a class that has a <code>__call__</code> method, but still has a name?
I'd like to be able to do this:
<code>print Fun().__name__
</code>
and have it print <code>Fun</code>.


A:

You can define a function with a <code>__name__</code> attribute:
<code>class Fun(object):
    def __call__(self):
        return 42

    def __getattr__(self, attr):
        if attr == "__name__":
