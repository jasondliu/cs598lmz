import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
</code>
It works fine and prints <code>&lt;__main__.CFUNCTYPE object at 0x7f3ecdc926e0&gt;</code>. However, if I copy and paste the code into the interpreter and type <code>fun</code>, it prints <code>&lt;__main__.FUNTYPE object at 0x7f3ecdc926e0&gt;</code>. What is the difference between these two types? When are each appropriate to use?


A:

It's the same thing. When the docs say you can use a <code>CFUNCTYPE</code> object wherever a <code>callback</code> is expected, accept <code>callback</code> as meaning either <code>CFUNCTYPE</code> or <code>callback</code>.
The distinction seems to be that <code>callback</code> is an alias for <code>CFUNCTYPE</code> that is meant to be used in place of the function type. For example:
<code>ctypes.windll.kernel32.SetProcessWorkingSetSize(-
