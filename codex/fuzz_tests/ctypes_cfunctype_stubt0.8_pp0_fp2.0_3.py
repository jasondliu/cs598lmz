import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0
</code>

When I load this module using PyRun_SimpleFile() in Python 3.4 I get the following error:
<code>TypeError: a bytes-like object is required, not 'int'
</code>
This seems to have something to do with the fact that the file has been opened in binary mode when using PyRun_SimpleFile(), but I have not been able to figure out a way around this.

If I load the same module using PyImport_ExecCodeModule() from a script with the following code, it works fine:
<code>with open("foo.c", "rb") as f:
    code = f.read()
codeobj = compile(code, "foo.c", "exec")
foo = PyImport_ExecCodeModule("foo", codeobj)
</code>

So my question is how do I make PyRun_SimpleFile() work with the code above?


A:

You can not use <code>PyRun_SimpleFile</code> on a file containing C code - this is an API error.
<blockquote>
<p>Return a new code object
