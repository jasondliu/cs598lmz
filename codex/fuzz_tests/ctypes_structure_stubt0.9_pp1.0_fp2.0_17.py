import ctypes

class S(ctypes.Structure):
    x = ctypes.create_string_buffer(b"hello")
S(b"world")
</code>
This is actually allowed, and quite useful sometimes, as it can be a concise way to copy temporary objects that would otherwise be destroyed at the end of expressions.  For example, this can be used to initialize an array of structures:
<code>class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

data = (S(b"hello"), S(b"world"))
</code>
Note that unlike named variables, temporary objects can't legally be used on the LHS of assignment, so they'll always be "naturally" destroyed before the enclosing expression is, even if by-reference copies are needed.

