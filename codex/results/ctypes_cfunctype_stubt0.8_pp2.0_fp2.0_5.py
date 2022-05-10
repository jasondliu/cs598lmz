import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "foo"
</code>
This is fine. However, I'd like to make <code>fun</code> callable directly from C++. So far, I've tried using <code>boost::python::object</code>, but I get a <code>TypeError</code>:
<blockquote>
<p>TypeError: No to_python (by-value) converter found for C++ type: boost::python::object</p>
</blockquote>
I've also tried <code>PyObject*</code>, but that produces:
<blockquote>
<p>error: cannot convert ‘boost::python::api::object’ to ‘PyObject*’ in return</p>
</blockquote>
How can I make my function callable from C++?


A:

<code>PyObject</code> should work. Here's a minimal example.
test.cpp:
<code>#include &lt;Python.h&gt;
#include &lt;boost/python.hpp&gt;

PyObject* function_from_python();

BOOST_P
