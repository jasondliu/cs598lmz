import ctypes
ctypes.cast(int(1), ctypes.py_object)
</code>
The above line is from a library that I am trying to use. 
I have tried importing ctypes and casting the int as py_object but I am getting the following error:
<code>TypeError: an integer is required (got type int)
</code>
I have also tried importing ctypes.wintypes, ctypes.pythonapi, ctypes.c_long, ctypes.c_int but none of these work. 
I am using python 3.4.4 on windows 10. 


A:

I think you are supposed to do this: <code>ctypes.cast(ctypes.py_object(1), ctypes.py_object)</code>

