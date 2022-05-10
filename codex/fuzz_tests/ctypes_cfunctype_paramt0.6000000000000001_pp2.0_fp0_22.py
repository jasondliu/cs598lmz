import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def myfunc(x):
    return x

CMPFUNC = FUNTYPE(myfunc)

if __name__ == '__main__':
    import sys
    import random
    import time

    n = int(sys.argv[1]) if len(sys.argv) &gt; 1 else 5
    arr = [random.randint(1, n) for _ in range(n)]
    print 'input:', arr

    start = time.clock()
    arr.sort(cmp=CMPFUNC)
    end = time.clock()
    print 'output:', arr
    print 'time: %.6f' % (end - start)
</code>
With Python 2.7.3 on Windows 7, this is the output I get:
<code>C:\Code\Python&gt;python sort_func.py
input: [4, 1, 5, 3, 3]
output: [1, 3, 3, 4, 5]
time: 0.000018

C:\Code\
