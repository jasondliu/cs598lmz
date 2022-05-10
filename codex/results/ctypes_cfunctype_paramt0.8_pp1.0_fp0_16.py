import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def print_msg(msg):
    print "Python says: '%s'" % msg

c_print_msg = FUNTYPE(print_msg)

lib2 = ctypes.CDLL("./lib2.so")
lib2.print_msg(c_print_msg)
</code>
lib2.cpp
<code>#include &lt;iostream&gt;
#include &lt;string&gt;

extern "C" typedef int (*function)(const char*) ;

int print_msg(function call, const char* msg)
{
    return call(msg) ;
}

void py_call(function call)
{
    print_msg(call, "Hello from C++") ;
}

extern "C" void print_msg(function call)
{
    py_call(call) ;
}
</code>
and the Makefile:
<code>all: lib1 lib2

lib1:
    g++ -shared -o lib1
