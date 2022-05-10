import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double()
    y = ctypes.c_float()

p = ctypes.pointer(S())
p.contents.x
p.contents.y
</code>
Why do I have to use "contents" and not just access the value directly?
What is happening behind the scenes here?


A:

The type <code>ctypes.POINTER(&lt;type&gt;)</code> is a pointer to the structure, not a structure instance.  To access the contents of the pointer you need to access the <code>contents</code> attribute (or the <code>value</code> attribute, more on that below.)
As you've probably noticed, <code>ctypes</code> always returns pointer objects (of various types) when it interacts with C code.  These pointers, like their C counterparts, are just numerical addresses of objects in memory.  In order to access the actual object at these addresses -- or to pass them to a function, for that matter -- you need to access their <code>contents</code> or <code>value</code> attributes.
This is in contrast to <
