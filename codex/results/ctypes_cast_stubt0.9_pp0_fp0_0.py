import ctypes
ctypes.cast(aA, ctypes.py_object).value
</code>
but this also fails, with the error message 
<code>TypeError: cannot be converted to a Python object
</code>
I want to get a back a pointer, not the data cast to a NumPy array.


A:

Alas, PyArray_BYTES returns a buffer pointing to the raw data underlying the input NumPy array. That does not correspond to a memory location from which a pointer can be constructed, so there is no good way (with my current knowledge) to return a pointer to the raw data.
I've written up some other alternative methods for returning pointers to the raw data underlying NumPy arrays. I would be interested in seeing even cheaper methods than these, and also as to whether these techniques are good/bad practice.

