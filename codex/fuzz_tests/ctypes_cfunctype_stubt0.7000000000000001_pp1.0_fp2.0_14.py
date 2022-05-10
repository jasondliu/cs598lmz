import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"
</code>
Next, I use SWIG to wrap the function <code>fun</code> into a C module:
<code>// file hello.i
%module hello
%{
#include "hello.h"
%}

%include "hello.h"
</code>
where <code>hello.h</code> is:
<code>#include &lt;Python.h&gt;
PyObject *fun();
</code>
The generated wrapper works fine for the function <code>fun</code>:
<code>&gt;&gt;&gt; import hello
&gt;&gt;&gt; hello.fun()
'hello world'
</code>
The problem is that SWIG generated a wrapper for <code>FUNTYPE</code> too:
<code>&gt;&gt;&gt; hello.FUNTYPE
&lt;Swig Object of type 'CFUNCTYPE *' at 0x7f9e9b2d1e80&gt;
</code>
It seems that SWIG's default behaviour is to expose everything in
