import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double(1)

i = 0
while True:
    i += 1
    if i % 100 == 0:
        print i
    S()
</code>
I'm running CPython and a 64-bit version of Windows. I don't think the particular version of Python matters. I'm using Python 2.7.4.
Edit: I just ran this code on Linux and Mac OS. I did not observe the memory leak, and the <code>SIZE</code> stayed below 1,000 bytes. I also tried running this code on 64-bit versions of Linux and Mac OS, and I also did not observe a memory leak. I don't really understand why this code leaks on Windows. Is it possibly a bug in the Python interpreter?
Edit 2: The memory leak is not caused by the <code>ctypes.Structure</code> objects, as the following code demonstrates.
<code>from sys import getsizeof

i = 0
while True:
    i += 1
    if i % 100 == 0:
        print i
    getsizeof(i)
</code>
This code runs on Windows and Linux
