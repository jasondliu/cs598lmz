import ctypes
ctypes.cast(block, ctypes.py_object).value = 'x'*500
</code>
But I am still not able to use ctypes in my cpp program to access the data stored in the block.
I want to get the block as a <code>void*</code> in my cpp program and then cast it to <code>PyObject *</code> so I can use some functions from python API to convert the data to cpp formats.
I am not able to find the equivalent to <code>block</code> in cpp code.
Can someone help me out here?

