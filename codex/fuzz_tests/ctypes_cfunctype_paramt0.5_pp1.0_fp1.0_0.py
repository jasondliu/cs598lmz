import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def foo(a,b):
    return a+b

foo_c = FUNTYPE(foo)
print foo_c(1,2)
</code>
Is there a way to do this in C++? I tried the following:
<code>#include &lt;iostream&gt;
#include &lt;functional&gt;

using namespace std;

int foo(int a, int b) { return a+b; }

int main() {
    function&lt;int(int,int)&gt; foo_c = foo;
    cout &lt;&lt; foo_c(1,2) &lt;&lt; endl;
    return 0;
}
</code>
But I get this error:
<code>g++ -std=c++11 foo.cpp -o foo.out
/usr/include/c++/4.8/functional: In instantiation of ‘struct std::_Bind_simple&lt;int (*(int, int
