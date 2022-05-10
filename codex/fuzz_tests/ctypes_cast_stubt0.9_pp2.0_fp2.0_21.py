import ctypes
ctypes.cast(0, ctypes.py_object)

#Also this produces a different error
data_section_addr = ctypes.cast(0, ctypes.py_object)
</code>
The first line produces this error:
   ctypes.ArgumentError: argument 1: : wrong type
Running the second line produces this error:
    ctypes.ArgumentError: argument 2: : Don't know how to convert parameter 2
Can anyone point me in the right direction? 
Thanks!

