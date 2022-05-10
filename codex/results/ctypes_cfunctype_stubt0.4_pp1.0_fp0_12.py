import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
print(fun())
</code>
This segfaults.
I'm using Python 3.6.5 on Ubuntu 18.04.1 LTS.
I'm using the system's Python, which was installed by apt.
<code>$ python3.6 --version
Python 3.6.5
$ python3.6 -c 'import sys; print(sys.version)'
3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0]
</code>
I'm using the system's ctypes, which was installed by apt.
<code>$ python3.6 -c 'import ctypes; print(ctypes.__version__)'
1.1.0
</code>
I'm using the system's libpython, which was installed by apt.
<code>$ ldd /usr/bin/python3.6 | grep libpython
        libpython3.6m.so.1.0 =&gt; /usr/lib/x86_64-linux-gnu/libpython3.6m.so.1.
