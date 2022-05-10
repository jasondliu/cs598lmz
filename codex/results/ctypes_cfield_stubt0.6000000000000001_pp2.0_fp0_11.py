import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.x = 1

c = C()

a = ctypes.cast(id(c.x), ctypes.POINTER(ctypes.CField))

c.x = 2

print(a.contents.value)

print(ctypes.cast(a, ctypes.POINTER(C)).contents.x)
</code>
This works, but I am wondering if there is a better way of doing this.


A:

I don't think there is any "better" way of doing this.
But you might want to consider a couple of things:

you don't need to cast the <code>id()</code> to a pointer, you can just pass it to <code>addressof()</code> directly
you can replace <code>C</code> with a <code>ctypes.Structure</code> subclass

The following works:
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_
