import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int8()
    y = ctypes.c_int8()

ctypes.pointer(S())

class S2(ctypes.Structure):
    x = ctypes.c_int16()
    y = ctypes.c_int16()

ctypes.pointer(S2())
</code>
All 4 lines compile with no exception (<code>UnicodeDecodeError</code>). The same was observed with:

A CPython 2.7.10 container, built with <code>docker run -t -i python:2.7.10 /bin/bash</code>
A Dockerfile based on <code>ubuntu:latest</code>, using the following <code>RUN</code> statement (<code>python2</code> comes from <code>apt-get</code>):
<code>RUN python2 -c "from ctypes import *;class S(Structure): x = c_int8, y = c_int8;pointer(S());class S2(Structure): x = c_int16(), y = c_int16();pointer(S
