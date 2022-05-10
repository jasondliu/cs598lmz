import ctypes
ctypes.cast(ptr, ctypes.py_object).value

# open up a new subsession from the top session
sess2 = numpy.empty((), dtype=numpy.object_)
sess2[()] = top.as_numpy_array(sess2)

# what happens when we call eval?
sess2[()].eval(x).as_ndarray()
</code>

