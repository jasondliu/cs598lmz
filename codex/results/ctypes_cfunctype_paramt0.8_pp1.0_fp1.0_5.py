import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
def pyfun(x):
    print(x)
def pyfun2(x):
    print(x*2)

cfun1 = FUNTYPE(pyfun)
cfun2 = FUNTYPE(pyfun2)
</code>
If I do 
<code>cfun1(2)
</code>
it prints 2
But if I do 
<code>cfun1(3)
cfun2(3)
</code>
it just prints 3 and it throws nothing.
In the console I see "Process finished with exit code 0" and nothing else


A:

Use <code>sys.stdout.flush()</code> to flush Standard Output.
Adding something like this before your loop might help:
<code>import sys
import time
while True:
    ...
    time.sleep(0.01)  # Sleep 100 ms
    sys.stdout.flush()
</code>

