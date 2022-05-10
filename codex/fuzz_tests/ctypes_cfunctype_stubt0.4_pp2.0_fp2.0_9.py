import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
And it works:
<code>$ python3 test.py
42
</code>
Now I want to call this function from C. I've tried:
<code>#include &lt;Python.h&gt;

int main()
{
    PyObject *pModule, *pFunc;
    PyObject *pArgs, *pValue;

    Py_Initialize();
    pModule = PyImport_ImportModule("test");
    pFunc = PyObject_GetAttrString(pModule, "fun");

    pValue = PyObject_CallObject(pFunc, NULL);
    printf("%ld\n", PyLong_AsLong(pValue));

    Py_Finalize();
    return 0;
}
</code>
But it gives me a segfault:
<code>$ gcc -o test -I/usr/include/python3.6m -lpython3.6m test.c
$ ./test
Segmentation fault
</code>
What am I doing wrong?


A:

