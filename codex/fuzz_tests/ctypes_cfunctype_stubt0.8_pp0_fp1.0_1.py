import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
def fun2(lib):
    return getattr(lib, "fun")()

fun2.restype = ctypes.py_object
import ctypes
lib = ctypes.CDLL("./libcc.so")
fun2(lib)

import ctypes
lib = ctypes.CDLL("./libcc.so")
print(fun2(lib))
</code>
The above code works only if I have the <code>fun()</code> function declared in C. In fact, I don't want to declare fun() in C. I want the python function fun() to be called with the variable name <code>fun</code>.
My ./libcc.so was generated with the following commands:
<code>gcc -Wall -c -fPIC fun.c -o fun.o
gcc -shared -o libcc.so fun.o
</code>
where fun.c is:
<code>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
char * fun()
{
  return
