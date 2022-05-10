import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
</code>
This works fine.
However, I want to return a string with a value depending on the argument.
<code>def fun(i):
    return "hello" + str(i)
</code>
This does not work.
<code>TypeError: CFUNCTYPE() argument 1 must be callable
</code>
How can I pass a variable to the function?


A:

You need to create a closure, i.e. a function that returns the actual function you want to call.
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

def fun(i):
    return "hello" + str(i)

@FUNTYPE
def fun_closure(i):
    return fun(i)
</code>
This works, but the returned function is slow:
<code>&gt;&gt;&gt; fun_closure(1)
'hello1'
&gt;&gt;&gt; fun_closure(1)
'hello1'
&gt;&gt
