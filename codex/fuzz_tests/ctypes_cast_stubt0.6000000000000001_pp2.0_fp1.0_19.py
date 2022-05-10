import ctypes
ctypes.cast(1, ctypes.py_object)

#Create a new ctypes instance from the Python Object
int_a = ctypes.py_object(1)

#Convert ctypes instance to integer
int(int_a)

#Convert integer to ctypes instance
ctypes.py_object(5)

#Get the address of the object
id(5)

#Convert the address to an integer
int(id(5))

#Convert the integer back to an object
ctypes.cast(10914624, ctypes.py_object)

#Create a new ctypes instance from the Python Object
int_a = ctypes.py_object(1)

#Convert ctypes instance to integer
int(int_a)

#Convert integer to ctypes instance
ctypes.py_object(5)

#Get the address of the object
id(5)

#Convert the address to an integer
int(id(5))

#Convert the integer back to an object
ctypes.cast(10914624, ctypes.py_object)
