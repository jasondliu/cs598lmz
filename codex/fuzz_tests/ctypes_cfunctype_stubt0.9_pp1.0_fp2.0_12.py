import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'Hello World!'

CFUNCTYPE = ctypes.CFUNCTYPE
def build_fun(cfun):
    return CFUNCTYPE(ctypes.py_object)(cfun)

if __name__ == '__main__':
    cfun = CFUNCTYPE(ctypes.py_object)(fun)
    print(type(cfun), type(fun), type(build_fun(fun)))
    print(cfun(), fun(), build_fun(fun)())
</code>
And the output is:
<code>&lt;class 'ctypes.CFUNCTYPE'&gt; &lt;class 'method'&gt; &lt;class 'ctypes.CFUNCTYPE'&gt;
Hello World! Hello World! Hello World!
</code>
I know this is not Pythonic but why does this happen?


A:

CPython uses two different types of method objects.

<code>function</code> objects are ones that don't have a class, like your <code>build_fun</code> function:
<
