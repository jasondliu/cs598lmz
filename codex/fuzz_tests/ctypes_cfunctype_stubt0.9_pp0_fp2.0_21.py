import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()
</code>
I get the following error:
<code>Segmentation fault (core dumped)
</code>
This only happens for <code>None</code>, <code>True</code> and <code>False</code>. Any other object is ok.
Does anyone know why this happens?


A:

<code>None</code>, <code>True</code> and <code>False</code> are singletons, i.e. there is no way to create a PyObject* for them other than getting the address of the static object. This normally isn't a problem, even though their addresses may change from run to run, since there's a shared table of objects that the interpreter knows to use; this table is usually generated at build time.
The problem is that the table is set up before any extension modules are loaded, so it only knows about the built-in types. This is a problem in your case, since you've extended the interpreter using <code>ctypes</code>, so your module gets loaded after the static list of objects has been populated. The result is that <code>Py_BuildValue()</code>
