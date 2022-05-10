from types import FunctionType
a = (x for x in [1])
b = True
c = print
d = 'hello'
e = [1, 2, 3]
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print('----end')

## for a primitive type in Python such as integers or floats,
#  we cannot change the object (in mutable data structures 
#  we would say that the object is immutable)

# DEFINITIONS
# Object: any type and instance of the type
# Instance: the individual objects created by using the class

# Definition of class
# A class is a user-defined type
# they provide the mechanism for creating objects
# and a namespace for defining methods that operate on instances of that class

# Defining Classes - very similar to Java, one important difference 
# is that generally no explicit constructor is defined in Python

# CLASS DEFINITION SYNTAX
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

# HOW
