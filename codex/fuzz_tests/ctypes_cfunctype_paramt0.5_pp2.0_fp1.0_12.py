import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(x, y):
    print "callback called with %d, %d" % (x, y)
    return x + y

callback_func = FUNTYPE(callback)

print "result: %d" % (lib.add_callback(callback_func))
</code>
The C code:
<code>#include &lt;stdio.h&gt;

typedef int (*callback_t)(int x, int y);

int add_callback(callback_t callback)
{
    return callback(1, 2);
}
</code>
The CMakeLists.txt:
<code>cmake_minimum_required(VERSION 2.6)
project(test)

add_library(test SHARED test.c)

add_executable(test_exe test.py)

set_target_properties(test_exe PROPERTIES LINKER_LANGUAGE CXX)

target_link_libraries(test_exe test)

