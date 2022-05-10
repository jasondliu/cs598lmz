import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

cfunc = FUNTYPE(func)

print cfunc(1, 2)
</code>
This works fine if I call <code>cfunc</code> from Python. However, if I try to call <code>cfunc</code> from C, I get a segmentation fault.
<code>#include &lt;stdio.h&gt;
#include &lt;Python.h&gt;

int main(int argc, char *argv[])
{
    Py_Initialize();
    PyRun_SimpleString("import test\nprint test.cfunc(1, 2)");
    Py_Finalize();
    return 0;
}
</code>
I compile this with <code>gcc -o test test.c -I/usr/include/python2.7 -lpython2.7</code>.
I'm running Python 2.7.3 on Ubuntu 12.04.
What am I doing wrong?
