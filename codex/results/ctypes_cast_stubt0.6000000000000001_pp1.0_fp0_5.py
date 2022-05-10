import ctypes
ctypes.cast(pointer, ctypes.py_object).value
</code>
This works, but it's kind of clumsy.
I also considered using the <code>re</code> module to parse the output of <code>objdump</code>, but that would be a lot of work, and would be very dependent on the exact output of <code>objdump</code>.
Can anyone think of a better way to do this?


A:

This is an old question, but I don't think it's been answered properly.
If you have a pointer to a PyObject, you can use the <code>from_address</code> function in the <code>ctypes</code> module to get a reference to the object.
<code>from ctypes import py_object, c_void_p, pythonapi

def pyobject_from_address(address):
    return py_object.from_address(address)
</code>
This function works because, as explained in the PyObject_AS_GCALLOC documentation, "every PyObject has a pointer to its heap allocated memory".

