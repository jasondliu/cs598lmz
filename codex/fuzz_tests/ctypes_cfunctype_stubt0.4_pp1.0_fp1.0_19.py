import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class A(object):
    def __init__(self):
        self.f = fun

a = A()
a.f()
</code>
So, I'm trying to store a ctypes callback in an instance attribute.
This works fine on Python 2.7, but on Python 3.4, I get a <code>TypeError</code> when calling <code>a.f()</code>:
<code>TypeError: &lt;built-in method __call__ of CFUNCTYPE object at 0x7f9d9b4d7c80&gt; returned a result with an error set
</code>
What is going on?


A:

The problem is that <code>ctypes.py_object</code> is not a valid return type for a callback function on Python 3.  The documentation says:
<blockquote>
<p>On Windows, <code>&lt;code&gt;py_object&lt;/code&gt;</code> can only be used as a parameter type, not as a return type.</p>
</block
