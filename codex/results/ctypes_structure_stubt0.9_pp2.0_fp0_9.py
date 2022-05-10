import ctypes

class S(ctypes.Structure):
    x = ctypes.Union.__dict__['x'; self.x = 3]
ImportError: cannot import name x
</code>
Is this possible? Is it advisable? I want a structure that can switch between two types for the same bit field depending on one of their members.


A:

The closest analog to what you're looking for is an anonymous union.  First, the bits of python magic sauce... since we're going to be messing around with ctypes internals, we want to do it in the most pythonic way possible.  Declarators are just strings, right?  And strings are mutable, right?  So what we're going to do is construct a string and then "flux-capacitor" it with a time travel hack to insert the necessary code:
<code>import ctypes

x = "ctypes.Structure(('x', ctypes.c_char))"

x = x.replace(
    "ctypes.Structure(","ctypes.Structure(('union',ctypes.Union), ",1
    )

x = eval(x, globals(), locals())
</code>
This
