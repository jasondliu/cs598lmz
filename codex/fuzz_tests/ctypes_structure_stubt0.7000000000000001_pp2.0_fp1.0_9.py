import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint(0)
    y = ctypes.c_uint(1)

def f(s):
    return s.x

def g(s):
    return s.y

f(S()) # good
g(S()) # bad
</code>
When I run the program, I get the following error:
<code>$ mypy test.py
test.py:15: error: Argument 1 to "g" has incompatible type "S"; expected "S"
</code>
But I don't understand the error message. It doesn't make sense to me that the type-checker can see that <code>f</code> is passed an <code>S</code> when <code>g</code> is not.
If I put <code>cdef</code> in front of <code>S</code> and <code>f</code>, I get a warning about <code>S</code> being a struct. I'm not sure what that means.
What's going on? Is it a bug?
Edit:
It looks like this is a bug in mypy.



