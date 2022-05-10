import sys, threading
threading.Thread(target=lambda: sys.stdout.write(raw_input('C'))).start()
raw_input('A')
sys.stdout.write('B')
</code>
Run output:
<code>$ python threading_stdout.py
A
B
C
</code>
Now, the problem is that I'm trying to do this with a C++ program. So, I'm using C++11's threads:
<code>#include &lt;iostream&gt;
#include &lt;thread&gt;

int main()
{
    std::thread t([]() {
        std::cout &lt;&lt; getchar();
    });

    t.detach();

    std::cout &lt;&lt; "A";
    std::cout &lt;&lt; "B";
}
</code>
The problem is that I can't get it to work. With C++, the output is:
<code>$ ./threading_stdout
AB
</code>
See fiddle. Any idea how to fix this?


A:

You
