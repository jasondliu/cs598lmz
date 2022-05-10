import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
        print("I'm a python function in C")
# call the C function
cfun()
# call the Python function in the C code
fun()
</code>
Error message:
<code>Traceback (most recent call last):
  File "test.py", line 13, in &lt;module&gt;
    cfun()
  File "/usr/lib/python3.4/ctypes/__init__.py", line 366, in __call__
    return self.func(*args)
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
What's wrong?
Edit: Modified C code (Don't know why I need to add the <code>_</code>-prefix to the function names)
<code>#include &lt;Python.h&gt;

void _cfun(void)
{
        printf("I'm a C function\n");
}

PyObject* _fun(PyObject* self, PyObject* args)
{
        printf("I'm a python function in C\n");
