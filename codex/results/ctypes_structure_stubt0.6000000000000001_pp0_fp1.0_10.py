import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

def f(a):
    a.contents.x = 1
    a.contents.y = 2
    return a

s = S()
s_p = ctypes.pointer(s)
s_p = f(s_p)
print s_p.contents.x
print s_p.contents.y
</code>
I want to pass a pointer to a structure to a function, modify it and then return the pointer.
This is simply not working.
I get a "Segmentation fault" error.
What am I doing wrong?
PS: I know there are other ways to do that, but I need to do it like this.
Thanks


A:

I think you want <code>byref()</code> instead of <code>pointer()</code>.
<code>pointer()</code> returns a pointer to the pointer, not the thing being pointed at.
<code>&gt;&gt;&gt; s_p = f(ctypes.pointer(s))
&gt;
