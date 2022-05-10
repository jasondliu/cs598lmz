import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 4

print(fun())

def fun2():
    return 4

print(fun2())
</code>
The output is:
<code>4
4
</code>
It seems that the first function can return any kind of Python object, while the second function can only return an integer.
My questions are:

What is the internal difference between the two functions?
Is the first function slower than the second function?
What is the return type of the first function? If I want to specify the return type, can I do it?

Thanks.


A:

<blockquote>
<p>What is the internal difference between the two functions?</p>
</blockquote>
The first function is a C function, while the second is a Python function.
<blockquote>
<p>Is the first function slower than the second function?</p>
</blockquote>
Yes, because the C function needs to be called from Python, and the Python object needs to be created.
<blockquote>
<p>What is the return type of the first function? If I want to specify the return type,
