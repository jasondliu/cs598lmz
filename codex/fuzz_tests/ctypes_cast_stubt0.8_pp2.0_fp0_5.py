import ctypes
ctypes.cast("int", 1)

import ctypes
ctypes.pointer("int")
</code>
I have tried all of the following, but none of them worked.
<code>#include &lt;cstring&gt;
#include &lt;boost/python.hpp&gt;

using namespace boost::python;

struct xxx {
    xxx() : str("hello") {}
    char const* str;
};

BOOST_PYTHON_MODULE(ctypes_test)
{
    class_&lt;xxx&gt;("xxx")
        .def_readonly("str", &amp;xxx::str)
    ;
};
</code>
and
<code>#include &lt;cstring&gt;
#include &lt;boost/python.hpp&gt;

using namespace boost::python;

struct xxx {
    xxx() : str("hello") {}
    char const* str;
};

BOOST_PYTHON_MODULE(ctypes_test)
{
    class_&lt;xxx&
