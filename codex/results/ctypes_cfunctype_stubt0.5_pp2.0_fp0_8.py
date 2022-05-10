import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

class C(object):
    def __init__(self):
        self.f = fun

c = C()
print c.f()
</code>
I have an object <code>c</code> which has a method <code>f</code> which is a function created in C.
I want to be able to call <code>c.f()</code> in C++.
I am using the following code:
<code>#include &lt;Python.h&gt;
#include &lt;iostream&gt;

int main(int argc, char *argv[])
{
    Py_Initialize();

    // Import the file test.py
    PyObject* pName = PyString_FromString("test");
    PyObject* pModule = PyImport_Import(pName);

    // Get the c object
    PyObject* pDict = PyModule_GetDict(pModule);
    PyObject* pClass = PyDict_GetItemString(pDict, "C");
    PyObject* pInstance = Py
