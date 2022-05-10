import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): 
    return "Αναστάσης Τέρπτης"

lib.set_function(fun)

lib.test_print()
</code>
But it says the following:
<blockquote>
<p>AttributeError: type object 'PROPERTY_FUN' has no attribute 'from_address'</p>
</blockquote>
My <code>C++</code> code is as follows:
<code>#include &lt;cstdlib&gt;
#include &lt;iostream&gt;
#include &lt;string&gt;
#include &lt;boost/python.hpp&gt;


boost::python::object
get_fun()
{
    return boost::python::object();
}


void
set_fun(boost::python::object pycallback)
{
    pycallback();
}


BOOST_PYTHON_MODULE(boost_python_example)
{
    using namespace boost::python;
    def("get_fun", get_fun);
    def
