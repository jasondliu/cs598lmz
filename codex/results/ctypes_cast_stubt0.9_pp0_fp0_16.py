import ctypes
ctypes.cast(id(a), ctypes.py_object).value

#Peculiarities of Methods...

#Python lets you define methods for classes, but it does not explicitly support
#operator overloading. Methods can be called as functions, passed as arguments,
#mentioned in type specifiers, introspected and so on. The leading arguments of
#methods, though, are usually an object of some sort, so the fact that methods
#are really just functions means that they often wind up getting called in ways
#that are slightly different from plain functions.
#For example, the pickle module serializes objects by looking for their
#__getstate__ and __setstate__ methods. In order to know how to invoke these
#methods on an object, the pickle module has to first look up the class of the
#object and then get the appropriate method from the class.
#The pickle module knows how to do these things by calling special functions
#that are defined in the Python runtime. The following code shows how you might
#invoke the same functions yourself; in fact, it’s essentially a simplified
#version of the code that the pickle module
