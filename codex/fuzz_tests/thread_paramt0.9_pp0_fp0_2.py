import sys, threading
threading.Thread(target=lambda: sys.stdin.isatty()).start()
sys.exit()
</code>
Note that the crash is not caused by using Python threads from C:
<code>python3 -c 'import threading; threading.Thread(target=lambda: sys.stdin.isatty()).start()'
</code>
also makes a clean exit.
Any ideas are appreciated. Thanks.


A:

Found the reason: I was linking with a static Python. So it had its own malloc()/free() calls, provided by Python itself. When I was linking dynamically with libpython.so, Python was calling standard <code>malloc()</code>/<code>free()</code> and everything worked just fine.
So, I've compiled Python 3.9.0 with debug symbols (see this question and this one to get the details) and ran Python interpreter in a debugger:
<code>(gdb) run
Starting program: /home/avillagran/projects/python/python-3.9.0-debug/python 

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff
