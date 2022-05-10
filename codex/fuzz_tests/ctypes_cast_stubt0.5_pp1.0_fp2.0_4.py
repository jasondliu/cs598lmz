import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#2.
#The __dict__ attribute of the class will have the attribute name as key and the attribute value as corresponding value.

#3.
#The __doc__ attribute of the class will give us the documentation string.

#4.
#The __name__ attribute of the class will give us the class name.

#5.
#The __module__ attribute of the class will give us the module name in which the class is defined. This is __main__ in interactive mode.

#6.
#The __bases__ attribute of the class will give us the tuple of base classes.

#7.
#The __dict__ attribute of the class will give us the dictionary object of the class.

#8.
#The __class__ attribute of the class will give us the type of the class.

#9.
#The __call__ method enables Python programmers to write classes where the instances behave like functions.

#10.
#The __len__ method is called to implement the built-in function len(). Should return the length of the object, an integer
