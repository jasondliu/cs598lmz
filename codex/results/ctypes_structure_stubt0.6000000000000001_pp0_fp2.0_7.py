import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()

s = S()
s.x = ctypes.c_int(1)
s.y = ctypes.c_int(2)

print(s.x, s.y)
</code>
But I get the following error:
<code>AttributeError: '_ctypes.PyCapsule' object has no attribute 'x'</code>
Why is that?


A:

I think you are misunderstanding what <code>ctypes</code> is doing.  It's not creating a <code>Structure</code> subclass, it's creating a <code>Structure</code> instance.  You're then trying to assign to <code>x</code> and <code>y</code> on the <code>Structure</code> instance, which doesn't work.  You need to assign to the <code>Structure</code> instance's <code>x</code> and <code>y</code> attributes, which are <code>Field</code> instances:
<code>&gt;&gt
