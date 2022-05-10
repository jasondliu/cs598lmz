import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print fun()
print type(fun)
</code>
This works. However, I'd like to define the <code>fun</code> function in C. I tried putting the following in a C file:
<code>#include &lt;stdio.h&gt;
#include &lt;Python.h&gt;

PyObject *fun(void)
{
    PyObject * str = PyString_FromString("hello world");
    return str;
}
</code>
and then compiling it with <code>gcc -fPIC -shared -I/usr/include/python2.7/ -lpython2.7 -o myfun.so myfun.c</code>. However, when I try to load it from Python:
<code>import ctypes
fun = ctypes.CDLL('./myfun.so').fun
</code>
I get the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr
