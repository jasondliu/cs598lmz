import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

print(ctypes.CField)
print(ctypes.CField.__name__)
print(ctypes.CField.__module__)

import sys
print(sys.version)
</code>
<code>gdb</code> output:
<code>(gdb) r
Starting program: /Users/foobar/PycharmProjects/cfield/venv/bin/python /Users/foobar/PycharmProjects/cfield/main.py 
[Inferior 1 (process 71755) exited normally]

Process exited with status 0
</code>
<code>valgrind</code> output:
<code>==71776== Memcheck, a memory error detector
==71776== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==71776== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
==71776== Command: ./venv/bin/python main.py
==71776== 
&lt;class 'ct
