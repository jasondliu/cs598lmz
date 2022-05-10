import ctypes
ctypes.windll.user32.MessageBoxW(0, "Hello", "title", 1)
</code>
This works fine but when I try to call the same function from my C++ application I get a messagebox with the "Hello" text but the "title" does not appear.
My code:
<code>Py_Initialize();
PyObject *pModule = PyImport_ImportModule("myTest");
if (pModule == NULL)
{
    PyErr_Print();
}

PyObject* pFunc = PyObject_GetAttrString(pModule, "Hello");
if (pFunc &amp;&amp; PyCallable_Check(pFunc))
{
    PyObject_CallObject(pFunc, NULL);
}
Py_Finalize();
</code>
From what I've read I might need to pass a PyObject to the function but I'm not sure how. 
Can anyone help me please?


A:

If you read Python/C API Reference, you will find only 3 examples of arguments passed from Python to C.
You can pass only:

int

