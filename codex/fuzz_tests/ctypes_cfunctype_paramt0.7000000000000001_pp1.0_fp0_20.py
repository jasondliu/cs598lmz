import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None,ctypes.c_int)

# Wrapper for C++ function.
def my_callback(num):
    print "my_callback called"

# Cast python function to CFUNCTYPE.
cfunc = FUNTYPE(my_callback)

# Call the C++ function.
cpp_module.do_something(cfunc)
</code>
C++
<code>#include &lt;iostream&gt;

void my_callback(int num)
{
    std::cout &lt;&lt; "my_callback called" &lt;&lt; std::endl;
}

void do_something(void (*callback)(int))
{
    callback(0);
}
</code>

