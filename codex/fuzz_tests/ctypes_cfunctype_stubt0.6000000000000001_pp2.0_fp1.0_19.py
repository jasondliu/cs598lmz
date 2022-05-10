import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello world'
</code>
However, the result is not what I expected:
<code>&gt;&gt;&gt; fun()
'hello world'
&gt;&gt;&gt; fun.__name__
'fun_ptr'
&gt;&gt;&gt; fun.__doc__
'&lt;no doc&gt;'
</code>
I want to use the function in a module, but the <code>__name__</code> and <code>__doc__</code> are not what I want. Is there any way to solve this problem?


A:

You can't.
Here is the relevant code from <code>ctypes</code> that creates the actual function:
<code>if prototype is not None:
    tp = prototype
    if not isinstance(tp, _CFuncPtr):
        tp = _CFuncPtr(tp)
    if not tp._flags_ &amp; FUNCFLAG_CDECL:
        raise TypeError("Only CDECL functions are supported")
    if tp._flags_ &
