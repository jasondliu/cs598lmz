import ctypes
ctypes.cast(p, ctypes.py_object).value  # use ctypes to get the value of p
 
</code>
This is safe because the <code>PyObject.</code> structure definition is visible in the header file <code>pystate.h</code>, the <code>PyObject.</code> definition is <code>Py_buffer</code>, and the <code>Py_buffer</code> definition is visible in the header file <code>pystate.h</code>. (I verified that this is true in Python 3.7.0.)
This is probably not (at least not fully) a solution to your problem, but I just wanted to share this information with the world. If someone can prove that this isn't valid generally, even on the most common Python versions, please edit this answer.

