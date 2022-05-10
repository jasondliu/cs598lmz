import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
print(fun())
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    print(fun())
TypeError: 'PyCFuncPtr' object is not callable
</code>
Why isn't <code>fun</code> callable?


A:

You can't just use <code>ctypes</code> like that. You need to create a C library that defines the function you want to call. Here's an example:
<code>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

char * fun() {
    char * s = malloc(sizeof(char) * 6);
    s[0] = 'h';
    s[1] = 'e';
    s[2] = 'l';
    s[3] = 'l';
    s[4] = 'o';
    s[5] = '\0';
    return s;

