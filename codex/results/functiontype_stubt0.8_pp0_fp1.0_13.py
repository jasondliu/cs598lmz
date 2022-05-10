from types import FunctionType
a = (x for x in [1])
type(a)

#here, we apply the issubclass() method to determine whether the function class is a subclass of the object class.
#The issubclass() method returns Boolean value, True or False.

#issubclass(object, classBegin)

#Return true if the object argument is a subclass of the classinfo argument, or if the object argument
#is an instance of the classinfo argument. If object is not a class, returns false. If object is a class,
#returns true if classinfo is the same class or a base class of object.

issubclass(FunctionType,object)



# The isinstance() Function
#
# The isinstance() function is used to determine whether an object is an instance of a class or not.
#
# The syntax of the isinstance() function is:
#
# isinstance(object, classinfo)



# The Python isinstance() function returns True if the object is an instance of the specified class.
# Otherwise, it returns False.

# The isinstance() function checks if the object argument is an instance or subclass of classinfo argument.

