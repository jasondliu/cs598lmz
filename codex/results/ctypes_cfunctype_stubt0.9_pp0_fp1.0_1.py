import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    a = ctypes.c_ushort(-1)
    b = a.value % 2
    return b
</code>
This is the code I would like to use, via python callbacks, to get data from a C module.
Here is a simplified version of the C module:
<code>int a(int (*fp_a)()) {
    int a = fp_a();
    return a * 2;
}
</code>
The error I get when I run <code>python setup.py build</code> is
<code>clang: error: no such file or directory: 'build/temp.macosx-10.9-intel-2.7/test.o'
clang: error: no such file or directory: 'build/temp.macosx-10.9-intel-2.7/test.o'
error: command 'clang' failed with exit status 1
</code>
As far as I know, I have everything installed correctly.
What am I doing wrong?


A:

To use native code with a python extension module try using cython instead:
