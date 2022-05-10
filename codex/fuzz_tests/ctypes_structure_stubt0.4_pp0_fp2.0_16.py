import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print(s.x)
print(s.y)
print(s.x + s.y)
</code>
I get the following output:
<code>0
0
0
</code>
I would like to use the same technique to access the members of a structure in a C++ program. I am using the following code:
<code>#include &lt;iostream&gt;
#include &lt;string&gt;

struct S {
    int x;
    int y;
};

int main() {
    S s;
    std::cout &lt;&lt; s.x &lt;&lt; std::endl;
    std::cout &lt;&lt; s.y &lt;&lt; std::endl;
    std::cout &lt;&lt; s.x + s.y &lt;&lt; std::endl;
}
</code>
I get the following output:
<code>0
0
