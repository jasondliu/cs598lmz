from _struct import Struct
s = Struct.__new__(Struct)
s.format = f
s.size = 24
s.unpack(buffer)
</code>
and that works great!
I'm trying to do the same thing in C++. I've been trying to use libpython, but all of the methods seem to be for interacting with python code from C/C++, not the other way around. So I can get a PyObject pointer to the _struct.Struct type, and I can call its <code>size</code> and <code>format</code> properties, which return PyObject pointers, which I can cast to <code>PyUnicodeObject *</code> and <code>PyIntObject *</code> respectively.
But I can't find any way of converting those <code>PyIntObject</code> structs back into <code>int</code>s, so I can't use <code>Struct.size</code> to get a malloc'd buffer of memory, like I do in the Python.
So if I can't use libpython to unpickle these things, how can I?
And why doesn't <code>CString</code> work on PyObject pointers? 

